"""
Wrapper for tcpdump. 

"""
import re
import sys
import time
import pktgen
import shared
import config
import subprocess
import state



def sniff_and_send():
    """
    Main entry point. Starts sniff for traffic while generating packets on the
    remote host. 
    
    Returns None.
    
    """
    # Calculate the necessary parameters. Work in bits.
    
    target_bw_bps = config.target_bw_Mbps * 1000 * 1000
    pkt_size_b = config.pkt_size * 8
    pkt_count = target_bw_bps * config.max_time / pkt_size_b
    gap_ns = pkt_size_b * (10**9) / target_bw_bps # nanoseconds

    # Sniff. Save the text output to check for kernel-dropped packets.    
    
    shared.run_cmd('tcpdump -i ', config.sniff_iface,
                   ' -vnnxStt -s 96 -w ', config.tmp_pcap_file, 
                   ' udp > /tmp/tcpdump.log 2>&1')
    time.sleep(2)

    # Send!
    
    p_pktgen = pktgen.send(pkt_count, config.pkt_size, 
                           gap_ns, config.flow_count)

    # Make sure pktgen runs no more than max_time.
    
    pktgen_start_time = time.time()
    elapsed_time = 0

    while elapsed_time <= config.max_time and p_pktgen.poll() is None:    
        
        elapsed_time = time.time() - pktgen_start_time
        time.sleep(1)    
        
        sys.stdout.write('\r%s sec left' % int(config.max_time - elapsed_time))
        sys.stdout.flush()
    
    print ''
    pktgen.stop_and_parse_result()

    # Wait a bit before terminating tcpdump. It's probably not getting new
    # packets any more. Send Ctrl+C to tcpdump.
    
    time.sleep(2)
    shared.run_cmd('pkill tcpdump').wait()
    
    # Parse the number of packets dropped by the kernel.
    
    global last_captured_pkt_count, last_dropped_pkt_count
    last_captured_pkt_count = last_dropped_pkt_count = None
    
    logf = open('/tmp/tcpdump.log')
        
    for line in logf:
                
        r = re.search('(\d+) packets received by filter', line)
        if r: state.tcpdump_recvd_pkt_count = int(r.group(1))
            
        r = re.search('(\d+) packets dropped by kernel', line)
        if r: state.tcpdump_dropped_pkt_count = int(r.group(1))
    
    logf.close()

    # Displays the result of tcpdump    
    assert None not in (state.tcpdump_recvd_pkt_count,
                        state.tcpdump_dropped_pkt_count)
    if config.verbose:
        print 'TCPDUMP - received packets:',
        print state.tcpdump_recvd_pkt_count,
        print 'dropped packets:',
        print state.tcpdump_dropped_pkt_count




def parse_pkt(pkt_func):
    """
    Loops to parse output from tcpdump. An example would be:

    [recvd_time     ]                 [   ] <- (flow_id + 10000)
    1329098408.055825 IP 192.168.1.20.10007 > 192.168.1.1.9: UDP, length 22
          0x0000:    4500 0032 066e 0000 2011 10e8 c0a8 0114 <- ignore
          0x0010:    c0a8 0101 2717 0009 001e 0000 be9b e955 <- ignore
          0x0020:    0000 066f 4f38 6ea6 000e 4402 0000 0000 
                     [seq_num] [tvsec  ] [tvusec ]
                    ... the rest of the lines can be ignored

    Each time a new packet arrives, invokes the pkt_func callback function. The
    pkt_func should have arguments (flow_id, seq_number, sent_time, recvd_time).
    This allows users to handle incoming packets, based on these four
    parameters, accordingly.
    
    Returns None.

    """    
    # Initialize fields to extract.
    recvd_time = flow_id = seq_num = tvsec = tvusec = None

    # Regex applied on udp header to extract recvd_time and flow_id.
    regex_udp = re.compile('(\d+\.\d+) IP .*\.(\d+) >')

    # Regex applied on the pktgen payload.
    regex_pktgen = re.compile('0x0020:\s+(.{10})(.{10})(.{10})')

    # Parse with tcpdump -r
    p_tcpdump = shared.run_cmd('tcpdump -nnxStt -r ', config.tmp_pcap_file,
                               stdout=subprocess.PIPE)

    for line in p_tcpdump.stdout:

        re_udp = regex_udp.search(line)
        if re_udp:
            recvd_time = float(re_udp.group(1))
            flow_id = int(re_udp.group(2)) - 10000
            continue

        re_pktgen = regex_pktgen.search(line)
        if re_pktgen:

            # Here, the seq_num is a global value. We need to convert it to a
            # per-flow sequence number.
            seq_num = _hex_to_int(re_pktgen.group(1))
            seq_num = seq_num / config.flow_count

            # Convert the recvd timestamp to float.
            tvsec = _hex_to_int(re_pktgen.group(2))
            tvusec = _hex_to_int(re_pktgen.group(3))
            sent_time = tvsec + tvusec / 1000000.0

            # We should have obtained all necessary fields to form a packet.
            assert None not in (recvd_time, flow_id)
            pkt_func(flow_id, seq_num, sent_time, recvd_time)

            # Reset all fields.
            recvd_time = flow_id = seq_num = tvsec = tvusec = None
                



def _hex_to_int(hex_str):
    """
    Converts a hex_str (which may have spaces) into int.

    """
    hex_str = hex_str.replace(' ', '')
    return int(hex_str, 16)



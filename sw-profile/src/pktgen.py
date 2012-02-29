"""
Wrapper functions for pktgen.

"""

import subprocess
import config
import shared
import state
import time
import re



def send(pkt_count=56, pkt_size=1400, delay=0, flow_count=1):
    """
    Sends packets. Returns a Popen handle.
    
    """        
    f = open('../script/pktgen_wrapper_template.sh')
    pktgen_script = f.read()
    f.close()

    # Replace the place-holders in pktgen_wrapper.sh with actual parameters.
    
    replacement_dict = {'[PKTGEN_PROC]': config.pktgen_proc,
                        '[PKTGEN_IFACE]': config.pktgen_iface,
                        '[PKT_COUNT]': str(pkt_count),
                        '[PKT_SIZE]': str(pkt_size),
                        '[DELAY]': str(delay),
                        '[MAX_PORT]': str((flow_count + 10000)),
                        '[SRC_IP]': config.source_ip_fake,
                        '[DST_IP]': config.dest_ip,
                        '[DST_MAC]': config.dest_mac
                        }
    pktgen_script = _replace_string_with_dict(pktgen_script, replacement_dict)
    
    f = open('/tmp/pktgen_wrapper.sh', 'w')
    f.write(pktgen_script)
    f.close()

    # Copy the file to pktgen host's tmp.
    
    p = shared.run_cmd('scp -q /tmp/pktgen_wrapper.sh ',
                       'root@', config.pktgen_host, ':/tmp; ',
                       'rm /tmp/pktgen_wrapper.sh')
    p.wait()

    # Execute the script remotely.

    state.pktgen_run_time = state.pktgen_sent_pkt_count = None
    
    return shared.run_ssh('chmod +x /tmp/pktgen_wrapper.sh; ', 
                          '/tmp/pktgen_wrapper.sh', 
                          hostname=config.pktgen_host)
    



def stop_and_parse_result():
    """ Terminates the pktgen process and parses the pktgen result. """
        
    shared.run_ssh('pkill -2 pktgen_wrapper',
                   hostname=config.pktgen_host).wait()
    time.sleep(2)

    (state.pktgen_run_time, state.pktgen_sent_pkt_count) = _parse_result()
        
    


def _pgset(value, pgdev):
    """
    Helper for send(). Sets values for /proc/.../pktgen/...
    
    """
    return 'echo ' + value + ' > ' + pgdev + '; '
    



def _replace_string_with_dict(in_str, in_dict):
    """
    Helper for send(). Replace keys with values in the string.
    
    """
    out_str = in_str
    for key in in_dict:
        out_str = out_str.replace(key, in_dict[key])
    return out_str




def _parse_result():
    """
    Parses the pktgen result file in /proc, extracts the actual run time (in
    second) and packet count and returns them as a tuple.

    We want to match the following line:
    Result: OK: 8648151(c650366+d7997785) nsec, 87129 (1400byte,0frags)
                [     ] <-exp time in us        [   ] <- pkt sent

    """
    p_proc = shared.run_ssh('cat ', config.pktgen_proc, config.pktgen_iface,
                            hostname=config.pktgen_host,
                            stdout=subprocess.PIPE)

    result_regex = re.compile('OK: (\d+)\(.*\) nsec, (\d+) \(.*\)')

    for line in p_proc.stdout:

        r_obj = result_regex.search(line)
        if r_obj:
            print 'Parsing pktgen result:', line
            return (int(r_obj.group(1)) / 1000000.0, int(r_obj.group(2)))

    raise Exception('Unable to parse pktgen result.')





if __name__ == '__main__':
    
    p = send(pkt_count=56**3)
    time.sleep(3)
    
    print 'kill'
    stop_and_parse_result()
    
    print 'last_run_time:', state.pktgen_run_time 
    print 'last_sent_pkt_count:', state.pktgen_sent_pkt_count

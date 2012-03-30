"""
Main config file for virtual OVS

"""
verbose = True

#===============================================================================
# Experiment Parameters
#===============================================================================

# Bytes of a single UDP packet.
pkt_size = 1400

# Number of concurrent flows. Packets are sent in a round-robin fashion. For
# example, for flow_count=N, packets of the following ports are sequentially
# sent: 0, 1, ..., N-1, 0, 1, ..., N-1, ....
flow_count = 10

# What aggregate bandwidth in Mbps we should send. Note the actual sent
# bandwidth may be different. The aggregate bandwidth is independent of the
# number of flows.
target_bw_Mbps = 1500

# For how long (seconds) pktgen should be sending packets.
max_time = 15

# Parameters of sliced samples.

init_slice_pkt_count = 2048
steady_slice_pkt_count = 65536
steady_slice_start_ratio = 0.66

#===============================================================================
# Network Settings
#===============================================================================


source_ip = '192.168.1.2'
dest_ip = '192.168.1.1'

source_mac = '00:0c:29:b5:01:5e'
dest_mac = '00:0c:29:40:31:f5'

# OpenFlow ports to which each machine is connected.
source_of_port = '1'
dest_of_port = '2'



#===============================================================================
# PKTGEN Settings
#===============================================================================

# Control IP
pktgen_host = '192.168.224.138'

# From where to send packets
pktgen_iface = 'eth2'

pktgen_proc = '/proc/net/pktgen/'

# Must not be the real source IP, or else we will be flooded with ICMP messages.
# Change the last number of the real source_ip to something else.
source_ip_fake = '192.168.224.150'



#===============================================================================
# OpenFlow Settings
#===============================================================================

# Where can we run the OpenFlow control utilities (i.e. dpctl).
ofctl_ip = '192.168.224.136'

# How can we connect to the switch
sw_connection = 'br0'

del_flow_cmd = 'ovs-ofctl del-flows ' + sw_connection + ' && echo del-flows OK'

dump_flows_cmd = 'ovs-ofctl dump-flows ' + sw_connection

add_rule_cmd = lambda rule: 'ovs-ofctl add-flow ' + sw_connection + ' \'' + rule + '\''
                          
# The port refers to the real UDP port, i.e. flow_id + 10,000.                                                        
new_rule = lambda udp_port_num: 'cookie=0, priority=65536, idle_timeout=1805,hard_timeout=0,udp,in_port=' + source_of_port + ',dl_vlan=0xffff,dl_vlan_pcp=0x00,dl_src=' + source_mac + ',dl_dst=' + dest_mac + ',nw_src=' + source_ip_fake + ',nw_dst=' + dest_ip + ',tp_src=' + str(udp_port_num) + ',tp_dst=9,actions=output:' + dest_of_port



#===============================================================================
# TCPDump Settings
#===============================================================================

sniff_iface = 'eth2'

# Where to save the pcap output of tcpdump. We will need to parse this file
# later.
tmp_pcap_file = '/tmp/tcpdump.pcap'            
                                            
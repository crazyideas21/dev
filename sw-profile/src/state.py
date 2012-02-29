"""
The state of the system. Stores globally available statistics.

"""

pktgen_run_time = None
pktgen_sent_pkt_count = None

tcpdump_recvd_pkt_count = None
tcpdump_dropped_pkt_count = None

# Keep track of statistics of each flow. Maps flow_id to
#                             {'count': 0, 'loss': None,
#                              'rtt_min': None, 'rtt_max': None, 
#                              'rtt_sum': 0.0, 'rtt_mean': None,
#                              'init_slice': [], 'steady_slice': [],
#                              'init_slice_rtt_mean': None,
#                              'init_slice_rtt_stdev': None,
#                              'steady_slice_rtt_mean': None,
#                              'steady_slice_rtt_stdev': None}
flow_stat = {}    

# Global statistics in the form of: 
# {'recv_count': 0, 'recv_time': None,
#                   'sent_count': None, 'sent_time': None,
#                   'recv_start_time': None, 'recv_end_time': None, 
#                   'recv_bw_Mbps': None, 'sent_bw_Mbps': None}
global_stat = {}

# Number of packets parsed.
parsed_pkt_count = None


#===============================================================================
# Displays the flow stat and global stat. For debugging only.
#===============================================================================

def print_stat():
    
    for k in sorted(global_stat):
        print k, ':', global_stat[k]

    print ''
            
    for flow_id in sorted(flow_stat.keys()):
        print ' * Flow ', flow_id
        stat = flow_stat[flow_id]
        for k in sorted(stat):
            v = stat[k]
            if isinstance(v, list):
                print ' ' * 8, k, ':', 'len =', len(v)
            else:
                print ' ' * 8, k, ':', v
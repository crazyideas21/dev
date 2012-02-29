"""
Experiment controller that sniffs (with tcpdump), sends packets (with pktgen),
and parses the received packets.

"""
import sys
import state
import config
import shared
import pickle
import tcpdump


# Based on pktgen actual run time and pkt count, estimates the length of a flow.
_est_flow_length = None

# Estimates the boundaries of init and steady slices.
_steady_slice_start_seq_num = None
_steady_slice_end_seq_num = None



def run():
    """ Main entry point. """

    global _est_flow_length
    global _steady_slice_start_seq_num, _steady_slice_end_seq_num

    # Initialize global variables
    
    state.flow_stat = {}
    state.global_stat = {'recv_count': 0, 'recv_time': None,
                         'sent_count': None, 'sent_time': None,
                         'recv_start_time': None, 'recv_end_time': None, 
                         'recv_bw_Mbps': None, 'sent_bw_Mbps': None}

    _est_flow_length = None
    _steady_slice_start_seq_num = None
    _steady_slice_end_seq_num = None

    # Start! Analyze packets.
    
    tcpdump.sniff_and_send()
    tcpdump.parse_pkt(_get_new_pkt)
    print ''
    
    # Analyze flows.
    
    for flow_id in sorted(state.flow_stat.keys()):
        _process_flow_stat(flow_id)
    
    # Analyze aggregate.
    
    g = state.global_stat
    g['sent_time'] = state.pktgen_run_time
    g['sent_count'] = state.pktgen_sent_pkt_count
    
    g['recv_time'] = g['recv_end_time'] - g['recv_start_time']
    g['recv_bw_Mbps'] = g['recv_count'] * config.pkt_size * 8 / g['recv_time'] / 1000000
    g['sent_bw_Mbps'] = g['sent_count'] * config.pkt_size * 8 / g['sent_time'] / 1000000






def save(pickle_file_name):
    """
    The saved pickle object is a dict with keys ['pkt_size', 'flow_stat',
    'flow_count', 'target_bw_Mbps', 'global_stat', 'max_time'], in which:

    """
    f_obj = open(pickle_file_name, 'w')
    pickle.dump({'global_stat': state.global_stat,
                 'flow_stat': state.flow_stat,
                 'flow_count': config.flow_count,
                 'pkt_size': config.pkt_size,
                 'max_time': config.max_time,
                 'target_bw_Mbps': config.target_bw_Mbps}, f_obj)
    f_obj.close()
    






def _process_flow_stat(flow_id):

    stat = state.flow_stat[flow_id]
    pkt_count = stat['count']

    stat['loss'] = _est_flow_length - pkt_count
    if pkt_count > 0:
        stat['rtt_mean'] = stat['rtt_sum'] / stat['count']
    else:
        stat['rtt_mean'] = 0

    init_slice = stat['init_slice']
    steady_slice = stat['steady_slice']
    init_slice.sort()
    steady_slice.sort()

    (stat['init_slice_rtt_mean'], stat['init_slice_rtt_stdev']) = \
        shared.get_mean_and_stdev([rtt for (_, rtt, _) in init_slice])

    (stat['steady_slice_rtt_mean'], stat['steady_slice_rtt_stdev']) = \
        shared.get_mean_and_stdev([rtt for (_, rtt, _) in steady_slice])









def _get_new_pkt(flow_id, seq_number, sent_time, recvd_time):
    """ Callback function for new packet. """
    
    if flow_id < 0:
        return
    
    # Print parse stats
    
    if state.parsed_pkt_count is None:
        state.parsed_pkt_count = 0
    else:
        state.parsed_pkt_count += 1

    if state.parsed_pkt_count & 0xFFF == 0:
        sys.stdout.write('\r%d packets left to parse.' % (state.tcpdump_recvd_pkt_count - state.tcpdump_dropped_pkt_count - state.parsed_pkt_count))
        sys.stdout.flush()

    # Set global stat

    g = state.global_stat
    
    g['recv_count'] += 1
    
    if g['recv_start_time'] is None: 
        g['recv_start_time'] = recvd_time    

    g['recv_start_time'] = min(g['recv_start_time'], recvd_time)
    g['recv_end_time']   = max(g['recv_end_time'], recvd_time)

    # Initialize per flow stat dict. A slice is an unsorted list of tuples
    # (seq_num, rtt, sent_time).
    
    if flow_id not in state.flow_stat:
        state.flow_stat[flow_id] = {'count': 0, 'loss': None,
                                    'rtt_min': None, 'rtt_max': None,
                                    'rtt_sum': 0.0, 'rtt_mean': None,
                                    'init_slice': [], 'steady_slice': [],
                                    'init_slice_rtt_mean': None,
                                    'init_slice_rtt_stdev': None,
                                    'steady_slice_rtt_mean': None,
                                    'steady_slice_rtt_stdev': None}

    # Stat that applies to the entire flow

    stat = state.flow_stat[flow_id]

    stat['count'] += 1
    rtt = recvd_time - sent_time
    stat['rtt_sum'] += rtt

    if stat['rtt_min'] is None:
        stat['rtt_min'] = rtt
    stat['rtt_min'] = min(stat['rtt_min'], rtt)
    stat['rtt_max'] = max(stat['rtt_max'], rtt)

    # Pre-compute the slice boundaries.

    global _est_flow_length
    global _steady_slice_start_seq_num, _steady_slice_end_seq_num

    if _est_flow_length is None:

        _est_flow_length = state.pktgen_sent_pkt_count / config.flow_count + 1
        
        _steady_slice_start_seq_num = int(_est_flow_length * config.steady_slice_start_ratio)
        
        _steady_slice_end_seq_num = min(_est_flow_length, _steady_slice_start_seq_num + config.steady_slice_pkt_count)

    # Set stat for the initial and steady-state slices. Identify which of the
    # two slices to which this packet belongs, based upon its sequence number
    # and sent time.

    if 0 <= seq_number < config.init_slice_pkt_count:
        stat['init_slice'] += [(seq_number, rtt, sent_time)]

    if _steady_slice_start_seq_num <= seq_number < _steady_slice_end_seq_num:
        stat['steady_slice'] += [(seq_number, rtt, sent_time)]
    





def test():

    import switch
    
    switch.reset_flow_table()
    assert switch.add_rules(config.flow_count) == config.flow_count    
    
    run()
    print state.global_stat






if __name__ == '__main__':
    test()
""" 
Main experiment controller. 

"""
import time
import state
import switch
import config
import shared
import datetime
import sniff_send_parse



def main():
    """ Starts the experiment. """

    # shared.sync_clocks()
    shared.error_log('New run: ' + str(datetime.datetime.now()))

    # Initialize output directories.
    shared.run_cmd('mkdir -p ../out-pickle')
    shared.run_cmd('mkdir -p ../out-graph')

    for flow_count in [100, 500, 1000, 1500]:

        for forward_bw in [1200]:

#            reset_state()            
#            try:
#                switch.reset_flow_table()
#                switch.add_rules(flow_count)
#            except Exception, err:
#                print 'Cannot add rules:', repr(err)
#                continue

            time.sleep(2)

            config.pkt_size = 1400
            config.flow_count = flow_count
            config.max_time = 60
            config.target_bw_Mbps = forward_bw

            shared.safe_run(run_and_save, 'direct')




def run_and_save(exp_name):
    """ Runs experiment and saves result in pickle. """

    exp_name += '-%sflows-%sMbps-%ssec' % (config.flow_count,
                                           config.target_bw_Mbps,
                                           config.max_time)
    print '\n' * 10, '=' * 80, '\n', exp_name, '\n', '=' * 80, '\n' * 2
    sniff_send_parse.run()
    sniff_send_parse.save('../out-pickle/%s.pickle' % exp_name)
    print '\n' * 3
    print exp_name + ' completed.'



def reset_state():
    """ Resets all variables in the global state. """
    
    state.pktgen_run_time = None
    state.pktgen_sent_pkt_count = None
    state.tcpdump_dropped_pkt_count = None
    state.tcpdump_recvd_pkt_count = None
    
    state.flow_stat = {}
    state.global_stat = {}
    state.parsed_pkt_count = None




if __name__ == '__main__':
    main()
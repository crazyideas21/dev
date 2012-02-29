"""
Plots graphs from existing pickle files.

"""

import boomslang
import pickle
import os
import shared
import config

# Name of experiment
EXP_NAME = ''

def main():
    """
    Loads all pickles and plots each of them to ./out-graph/.

    """
    for file_name in os.listdir('../out-pickle'):
        
        pos_pickle = file_name.find('.pickle')
        if pos_pickle == -1:
            continue

        exp_name = file_name[0 : pos_pickle]
        plot(exp_name)



def plot(exp_name):

    global EXP_NAME
    EXP_NAME = exp_name

    f = open('../out-pickle/%s.pickle' % EXP_NAME)
    stat_dict = pickle.load(f)
    f.close()

    print 'Plotting', EXP_NAME
    shared.safe_run(percentage_bw_flow_id, stat_dict)
    # rtt_flow_id(stat_dict)
    shared.safe_run(rtt_seq_three_special_flows, stat_dict)
    shared.safe_run(cdf_rtt, stat_dict)




def cdf_rtt(stat_dict):
    """
    Plots a CDF of RTTs of init and steady slices for flows 0, N/2, and N-1.

    """
    layout = boomslang.PlotLayout()
    flow_count = stat_dict['flow_count']

    flow_id = None
    for flow_id in [0, flow_count / 2, flow_count - 1]:

        if flow_id in stat_dict['flow_stat']:

            stat = stat_dict['flow_stat'][flow_id]
            init_slice = stat['init_slice']
            steady_slice = stat['steady_slice']

            # Place both graphs on the same row

            layout.addPlot(_get_cdf_plot(init_slice, 
                                         'Initial Slice for Flow #%d' % flow_id),
                           'row%d' % flow_id)
            layout.addPlot(_get_cdf_plot(steady_slice, 
                                         'Steady Slice for Flow #%d' % flow_id),
                           'row%d' % flow_id)

        else:
            flow_id = None

    if flow_id:
        layout.save('../out-graph/' + EXP_NAME + '_cdf_rtt.png')
    



def _get_cdf_plot(inslice, title):
    """ Helper for cdf_rtt(). """

    if len(inslice) == 0:
        return

    prob = 0
    step = 1.0 / len(inslice)

    # Sort slice based on rtt

    sorted_slice = [(rtt, seq) for (seq, rtt, _) in inslice]
    sorted_slice.sort()

    # Compute CDF

    scatter = boomslang.Scatter()
    plot = boomslang.Plot()

    for (rtt, seq) in sorted_slice:
        scatter.xValues += [rtt * 1000.0]
        scatter.yValues += [prob]
        prob += step

    plot.add(scatter)
    plot.setTitle(title)
    plot.setXLabel('Latency (ms)')
    plot.setYLabel('CDF')

    return plot




def percentage_bw_flow_id(stat_dict):
    """
    Plots percentage bandwidth delivered against flow ID as a scatter graph.

    """
    scatter = boomslang.Scatter()

    flow_count = stat_dict['flow_count']
    flow_pkt_count_target = stat_dict['global_stat']['sent_count'] / flow_count + 1

    flow_id = None
    for flow_id in sorted(stat_dict['flow_stat'].keys()):

        stat = stat_dict['flow_stat'][flow_id]
        scatter.xValues.append(flow_id)
        scatter.yValues.append(stat['count'] * 100.0 / flow_pkt_count_target)

    if flow_id is None:
        return # Nothing to plot

    # Compute aggr sent bandwidth to be displayed in title

    aggr_sent_bw = stat_dict['global_stat']['sent_count'] * 8.0 * \
        stat_dict['pkt_size'] / stat_dict['global_stat']['sent_time'] / 1000000

    plot = boomslang.Plot()
    plot.add(scatter)
    plot.setXLabel('Flow ID')
    plot.setYLabel('% Bandwidth Delivered')
    plot.setTitle(EXP_NAME + '\n(aggr sent bw: %.2fMbps)' % aggr_sent_bw)
    plot.save('../out-graph/' + EXP_NAME + '_percentage_bw_flow_id.png')








def rtt_seq_three_special_flows(stat_dict):
    """
    Plots the RTT-seq-number graphs for the 1st, middle and last flow.

    """
    flow_count = stat_dict['flow_count']

    layout = boomslang.PlotLayout()

    flow_id = None
    for flow_id in [0, flow_count / 2, flow_count - 1]:

        if flow_id in stat_dict['flow_stat']:

            (plot_init, plot_steady) = _rtt_seq(stat_dict, flow_id)

            layout.addPlot(plot_init, grouping='row%d' % flow_id)
            layout.addPlot(plot_steady, grouping='row%d' % flow_id)

        else:
            flow_id = None

    if flow_id:
        layout.save('../out-graph/' + EXP_NAME + '_rtt_seq_special_flow.png')



def _rtt_seq(stat_dict, flow_id):
    """
    Plots RTT vs sequence numbers, for a given flow_id. Produces two graphs, one
    for init slice and one for steady slice.

    """
    stat = stat_dict['flow_stat'][flow_id]
    init_slice = stat['init_slice']
    steady_slice = stat['steady_slice']

    if init_slice == []:
        init_slice = [(0, 0, 0)]
    if steady_slice == []:
        steady_slice = [(0, 0, 0)]

    # Fill in RTT = 0 points for missing packets in both slices, so that the
    # sequence numbers are continuous.

    flow_length = 1 + int(stat_dict['global_stat']['sent_count'] / \
                              stat_dict['flow_count'])

    init_end = min(config.init_slice_pkt_count, flow_length)
    steady_start = int(flow_length * config.steady_slice_start_ratio)
    steady_end = min(steady_start + config.steady_slice_pkt_count,
                     flow_length)

    _fill_lost_pkt(init_slice, 0, init_end-10)
    _fill_lost_pkt(steady_slice, steady_start+10, steady_end-10)

    # Add data.

    scatter_init = boomslang.Scatter()
    scatter_steady = boomslang.Scatter()

    (scatter_init.xValues, scatter_init.yValues) = _get_seq_rtt(init_slice)
    (scatter_steady.xValues, scatter_steady.yValues) = _get_seq_rtt(steady_slice)

    # Convert RTTs to ms.
    scatter_init.yValues = map(lambda x: 1000 * x, scatter_init.yValues)
    scatter_steady.yValues = map(lambda x: 1000 * x, scatter_steady.yValues)

    # Plot!

    plot_init = boomslang.Plot()
    plot_steady = boomslang.Plot()

    plot_init.add(scatter_init)
    plot_steady.add(scatter_steady)

    plot_init.setTitle(EXP_NAME + ' | flow_id = %d' % flow_id)
    plot_init.setYLabel('Latency (ms)')
    plot_init.setXLabel('Sequence Numbers')
    plot_steady.setXLabel('Sequence Numbers')

    return (plot_init, plot_steady)



def _fill_lost_pkt(in_slice, start, end):
    """
    Fills a slice with zero RTTs values for missing sequence numbers. 

    """
    if in_slice == []:
        return

    start_seq_num = seq_num = start

    while seq_num < in_slice[-1][0]:

        index = seq_num - start_seq_num
        (current_seq_num, _, _) = in_slice[index]
        missing_slice = [(seq, 0, 0) for seq in range(seq_num, current_seq_num)]
        in_slice[index : index] = missing_slice
        
        seq_num +=1

    # Extend the slice with zeroes if we haven't reached the desired length.

    while seq_num < end:
        in_slice += [(seq_num, 0, 0)]
        seq_num += 1




def _get_seq_rtt(in_slice):
    """
    Returns a tuple of two lists: one of sequence numbers, and the other of
    RTTs.

    """
    seq_num_list = []
    rtt_list = []

    for (seq_num, rtt, _) in in_slice:
        seq_num_list.append(seq_num)
        rtt_list.append(rtt)

    return (seq_num_list, rtt_list)





def rtt_flow_id(stat_dict):
    """
    Plots RTT vs flow_id. Produces two graphs, one for init_slice and the other
    for steady_slice.

    """
    scatter_init = boomslang.Line()
    scatter_steady = boomslang.Line()

    flow_id = None
    for flow_id in sorted(stat_dict['flow_stat'].keys()):

        scatter_init.xValues.append(flow_id)
        scatter_steady.xValues.append(flow_id)

        stat = stat_dict['flow_stat'][flow_id]

        # Initialize yErrors
        if scatter_init.yErrors is None:
            scatter_init.yErrors = []
            scatter_steady.yErrors = []

        # Convert RTTs into ms

        scatter_init.yValues.append(stat['init_slice_rtt_mean'] * 1000)
        scatter_init.yErrors.append(stat['init_slice_rtt_stdev'] * 1000)

        scatter_steady.yValues.append(stat['steady_slice_rtt_mean'] * 1000)
        scatter_steady.yErrors.append(stat['steady_slice_rtt_stdev'] * 1000)

    if flow_id is None:
        return # Nothing to plot

    # Plot!

    plot_init = boomslang.Plot()
    plot_steady = boomslang.Plot()

    plot_init.add(scatter_init)
    plot_steady.add(scatter_steady)

    plot_init.setTitle(EXP_NAME)
    plot_init.setYLabel('Latency (ms)')
    plot_init.setXLabel('Flow ID')
    plot_steady.setXLabel('Flow ID')

    layout = boomslang.PlotLayout()
    layout.addPlot(plot_init, grouping='topRow')
    layout.addPlot(plot_steady, grouping='topRow')
    layout.save('../out-graph/' + EXP_NAME + '_rtt_flow_id.png')





























if __name__ == '__main__':
    main()
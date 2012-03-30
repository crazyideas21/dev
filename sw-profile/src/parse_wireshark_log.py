import re
import boomslang

pkt_in_times = [0] * 1500
flow_mod_times = [0] * 1500

pkt_in_re = re.compile('\d+\s+(\d+\.\d+).*OFP\+PKTGEN.*Seq: (\d+)')
flow_mod_re = re.compile('\d+\s+(\d+\.\d+).*OFP\s+Flow Mod')
flow_mod_port_re = re.compile('TCP/UDP Src Port.*\((\d+)\)')

def new_pkt(buf):

    is_flow_mod = False
    time = None
    seq = None

    for line in buf:

        r = pkt_in_re.search(line)
        if r:
            time = float(r.group(1))
            seq = int(r.group(2)) - 1
            print 'pkt_in:', seq, time, line
            pkt_in_times[seq] = time
            return
            
        r = flow_mod_re.search(line)
        if r:
            time = float(r.group(1))
            is_flow_mod = True
            continue

        if is_flow_mod:
            r = flow_mod_port_re.search(line)
            if r:
                seq = int(r.group(1)) - 10000
                if seq < 0: return
                print 'flow_mod:', seq, time, line
                flow_mod_times[seq] = time
                is_flow_mod = False
                return


def main():

    buf = []

    f = open('install_rules_pcap.log')

    for line in f:

        index = line.find(chr(0x0c))
        if index > -1:
            new_pkt(buf[:])
            buf = []
        else:
            buf.append(line.strip())

    f.close()

    print '*' * 80

    print 'flow_mod:', len(filter(lambda x: x > 0, flow_mod_times))
    print 'pkt_in:',   len(filter(lambda x: x > 0, pkt_in_times))

    start = 0
    end = 1555

    scatter_mod = boomslang.Scatter()
    scatter_mod.color = "red"
    scatter_mod.marker = 'x'
    scatter_mod.xValues = range(1500)[start:end]
    scatter_mod.yValues = flow_mod_times[start:end]

    scatter_in = boomslang.Scatter()
    scatter_in.color = "blue"
    scatter_in.marker = 'x'
    scatter_in.xValues = range(1500)[start:end]
    scatter_in.yValues = pkt_in_times[start:end]

    p = boomslang.Plot()
    p.add(scatter_in)
    p.add(scatter_mod)
    p.setDimensions(width=10, height=16)
    p.save('pcap.png')
    



if __name__ == '__main__':
    main()

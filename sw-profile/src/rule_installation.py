"""
Tests how fast the switch can install new rules. Starts 3000 flows with inter-
packet gap G. Send 1 packet per flow. Check, at the end, how many rules there
are in the TCAM and the software table. Repeat with different G values.

"""

import tcpdump
import switch
import shared
import time

FLOW_COUNT = 3000

def send_and_count(pkt_size, gap_ms):
    """
    Sends 1500 flows, each of FLOW_LENGTH packets of size pkt_size, and with gap_ms in
    microseconds. Returns the number of rules in the TCAM and the software table.
    
    """
    
    switch.reset_flow_table() 
    
    tcpdump.sniff_and_send(pkt_count_arg=FLOW_COUNT,
                           pkt_size_arg=pkt_size, 
                           gap_ns_arg=gap_ms*(10**6), 
                           flow_count_arg=FLOW_COUNT)
    
    time.sleep(5)

    flow_table = switch.dump_tables(filter='')

    return (len(filter(lambda x: x.find('table_id=0') >=0, flow_table)),
            len(filter(lambda x: x.find('table_id=2') >=0, flow_table)))

    
    

def main():
    
    f = open('install_rules.log', 'w')
    
    for pkt_size in [64]:
        #for gap_ms in [1,5,10,20,50,100,200,400]:
        for gap_ms in [10]:
            
            print >> f, pkt_size, gap_ms,            
            for _ in range(1):
                print >> f, shared.safe_run(send_and_count, pkt_size, gap_ms),
                f.flush()
                
            print >> f, ''

    f.close()
                
        

if __name__ == '__main__':
    main()        

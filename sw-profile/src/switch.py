"""
Wrapper functions for the OpenFlow switch.

"""
import sys
import time
import config
import shared
import subprocess



def reset_flow_table():
    """
    Removes all entries from all the flow tables.
    
    """
    p = shared.run_ssh(config.del_flow_cmd,
                       hostname=config.ofctl_ip)
    p.wait()
    
    # Let system stabilize.
    time.sleep(4)
    


def dump_tables(filter='table_id=0'):
    """
    Returns a list of rules in the TCAM (table_id = 0).
    
    """
    p = shared.run_ssh(config.dump_flows_cmd,
                       hostname=config.ofctl_ip, stdout=subprocess.PIPE,
                       verbose=False)
    return [line for line in p.stdout if line.find(filter) >= 0]




def add_rules(rule_count):
    """
    Adds specified number of rules into the TCAM (table_id = 0). Ensures that
    fewer than 8 rules are added every second. Returns the number of rules added
    to the TCAM from this function call.
    
    """
    initial_flow_count = len(dump_tables())
    
    for flow_id in range(rule_count):
        
        port = flow_id + 10000
        p = shared.run_ssh(config.add_rule_cmd(config.new_rule(port)),
                           hostname=config.ofctl_ip, stdout=subprocess.PIPE,
                           verbose=False)
        p.wait()
        
        # Verifies the TCAM for every ten rules added.
        if flow_id % 10 == 0:
            assert len(dump_tables()) - initial_flow_count == flow_id + 1
            
            sys.stdout.write('\radd_rules: %d left' % (rule_count - flow_id))                                
            sys.stdout.flush()
    
    print ''    
    return len(dump_tables()) - initial_flow_count


    
    
if __name__ == '__main__':
    
    reset_flow_table()
    add_rules(1500)    

import math
import config
import subprocess


def run_cmd(*cmd_args, **kwargs):
    """
    Runs a command in shell. Returns the Popen handle. Passes kwargs to the
    subprocess.Popen() call. One could, for example, specify the value of
    'stdout'.

    """
    cmd_args_str = map(str, cmd_args)
    cmd_str = ''.join(cmd_args_str)
    
    verbose = config.verbose
    if 'verbose' in kwargs:
        verbose = kwargs['verbose']
        del kwargs['verbose']
    if verbose:
        print ' * Running: ' + cmd_str
        
    return subprocess.Popen(cmd_str, shell=True, **kwargs)



def run_ssh(*cmd_args, **kwargs):
    """
    Runs SSH. Need to specify these keyword arguments:
    - user: SSH user. If none, defaults to root.
    - hostname: SSH username.
    
    The cmd_args are what's actually run in the SSH session. The rest of the
    kwargs are passed into run_cmd().
    
    """
    user = 'root'
    if 'user' in kwargs:
        user = kwargs['user']
        del kwargs['user']
        
    hostname = kwargs['hostname']        
    del kwargs['hostname']
    
    args = ['ssh ', user, '@', hostname, ' "'] + list(cmd_args) + ['"']         
    return run_cmd(*args, **kwargs)
    


def sync_clocks():
    """
    Synchrnoizes the clock of local and remote hosts. TODO: This is really
    coarse and should be called once.

    """
    remote_proc = subprocess.Popen(['ssh', 'root@' + config.pktgen_host,
                                    'ntpdate -p 8 ntp.ucsd.edu'])
    local_proc = subprocess.Popen(['ntpdate', '-p', '8', 'ntp.ucsd.edu'])

    print 'Synchronizing clocks...'
    assert local_proc.wait() == 0 and remote_proc.wait() == 0




def get_mean_and_stdev(inlist):
    """ Returns the mean and stdev as a tuple. """

    length = len(inlist)
    if length < 2:
        return (0, 0)

    list_sum = sum(inlist)
    
    mean = float(list_sum) / length
    sum_sq = 0.0

    for v in inlist:
        sum_sq += (v - mean) * (v - mean)

    stdev = math.sqrt(sum_sq / (length - 1))
    return (mean, stdev)

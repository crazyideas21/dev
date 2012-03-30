import math
import config
import subprocess
import traceback
import datetime


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
    ntpdate_cmd = 'pkill ntpd; ntpdate -p 8 ntp.ucsd.edu'
    
    remote_proc = run_ssh(ntpdate_cmd, hostname=config.pktgen_host)
    local_proc  = run_cmd(ntpdate_cmd)
    
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




def safe_run(func, *args, **kwargs):
    """
    Executes a function and returns its result safely. Aborts and logs traceback
    to err.log upon error.
    
    """

    try:
        return func(*args, **kwargs)

    except Exception, err:
        error_log('Function %s, %s, %s' % (repr(func), repr(args), repr(kwargs)))
        error_log('Exception: %s, %s' % (err, repr(err)))
        error_log(traceback.format_exc())
        return None



def error_log(log_str):
    """ Logs error to err.log. """
    
    try:
        f = open('err.log', 'w')
        log_str = '[%s] %s' % (datetime.datetime.now(), log_str)
        print >> f, log_str
        print log_str
        f.close()

    except Exception, err:
        print 'Logging failed:', repr(err), str(err)
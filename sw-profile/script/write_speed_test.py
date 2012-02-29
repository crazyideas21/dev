import time
import sys
import os

ITI = 1024 * 1.5

def main():

    try:
        path = sys.argv[1]
    except:
        print 'Specify what path to write to.'
        return

    filename = path + '/big-file'
    try:
        f = open(filename, 'w')
    except Exception, e:
        print 'Cannot write:', repr(e), str(e)
        return

    chunk = '0' * 1024 * 32 # 32 KB
    start = time.time()

    for i in range(int(ITI)):
        f.write(chunk)
    f.close()

    end = time.time()
    print '%.2f' % (int(ITI) * 32 / (end-start) / 1024), 'MB/s'

    os.system('rm ' + filename)


if __name__ == '__main__':
    main()

from multiprocessing import Process
import os


def run_pro(name):
    print('Run child process name:%s id:%s' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process id:%s' % os.getpid())
    p = Process(target=run_pro, args=('Wjt',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end...')

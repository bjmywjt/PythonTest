from multiprocessing import Pool
import os, time, random


def long_task_run(name):
    print('task name: %s id: %s start.' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('task name: %s done in :%0.2f sec' % (name, end - start))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for n in range(5):
        p.apply_async(long_task_run, args=(n,))
    print('waiting for child process run')
    p.close()
    p.join()
    print('all child task done!!!')

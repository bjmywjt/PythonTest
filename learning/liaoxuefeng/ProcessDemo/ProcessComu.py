from multiprocessing import Process, Queue
import os, time, random


# 写数据进程
def write(q):
    print('Process(%s) start to write' % os.getpid())
    for s in ('A', 'B', 'C'):
        q.put(s)
        print('Write %s to Queue.' % s)
        time.sleep(random.random())


# 读数据进程
def read(q):
    print('Process(%s) start to read' % os.getpid())
    while True:
        s = q.get()
        print('Get %s from Queue' % s)


if __name__ == '__main__':
    # 存数据队列
    q = Queue()
    # 写进程实例
    p1 = Process(target=write, args=(q,))
    # 读进程实例
    p2 = Process(target=read, args=(q,))
    p1.start()
    p2.start()
    # 等读进程完成
    p1.join()
    # 手动退出读进程
    p2.terminate()

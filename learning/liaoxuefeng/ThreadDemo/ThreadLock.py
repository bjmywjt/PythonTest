import multiprocessing
import threading

balance = 0
lock = multiprocessing.Lock()


def change_bal(value):
    global balance
    balance = balance + value
    balance = balance - value


def run_thread(n):
    for x in range(300000):
        lock.acquire()
        try:
            change_bal(n)
        finally:
            lock.release()

            
if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

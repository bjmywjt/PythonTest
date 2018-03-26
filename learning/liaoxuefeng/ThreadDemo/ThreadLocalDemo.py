import threading

local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello, %s thread in %s' %(std, threading.current_thread().name))


def define_student(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=define_student, args=('WJT',), name='Thread-A')
t2 = threading.Thread(target=define_student, args=('ZS',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

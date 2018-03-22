import os

print('Process (%s) start work' % os.getpid())

pid = os.fork()
if pid == 0:
    print('I am Child Process (%s) and my Parent Process is (%s).' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just create a child Process (%s)' % (os.getpid(), pid))

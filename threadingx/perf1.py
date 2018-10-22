import threading
import time

ntimes = 100000000
def count(n):
    while n > 0:
        n -= 1

t1_start = time.time()
count(ntimes)
count(ntimes)
t1_end = time.time()
print('Sequential Execution time = {}'.format(t1_end-t1_start))

t1_start = time.time()
thread1 = threading.Thread(target=count, args=(ntimes,))
thread2 = threading.Thread(target=count, args=(ntimes,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
t1_end = time.time()
print('Threaded Execution time = {}'.format(t1_end-t1_start))
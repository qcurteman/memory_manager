import multiprocessing as mp
import time

ntimes = 10000000
def count(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':

    t1_start = time.time()
    count(ntimes)
    count(ntimes)
    t1_end = time.time()
    print('Sequential Execution time = {}'.format(t1_end-t1_start))

    t1_start = time.time()
    mp1 = mp.Process(target=count, args=(ntimes,))
    mp2 = mp.Process(target=count, args=(ntimes,))
    mp1.start()
    mp2.start()
    mp1.join()
    mp2.join()
    t1_end = time.time()
    print('Process Execution time = {}'.format(t1_end-t1_start))
import time
import threading

def countdown(name, count):
    while count > 0:
        print(name, ' : counting down ', count)
        count -= 1
        time.sleep(.5)
    print(name, ' : exit thread function')
    return True

t1 = threading.Thread(target=countdown, args=('t1', 10,))
t1.start()
t1.join()

t2 = threading.Thread(target=countdown, args=('t2', 20,))
t2.start()
t2.join()

print('Exit main thread')
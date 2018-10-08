import time
import threading

class CountdownThread(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            print(self.getName(), ': Counting down', self.count)
            self.count -= 1
            time.sleep(.5)
        print('exit thread', self.getName())
        return True
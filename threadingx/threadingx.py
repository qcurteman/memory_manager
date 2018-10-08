import threading

class Threadingx(object):
    count = 1000000
    lock = threading.Lock()
    x = 0

    @classmethod
    def addx(cls):
        with cls.lock:
            for i in range(cls.count):
                cls.x += 1
        print('exit from addx')

    @classmethod
    def subx(cls):
        with cls.lock:
            for i in range(cls.count):
                cls.x -= 1
        print('exit from subx')
import threading

x = 0
counter = 10000000

def addx():
    global x
    for i in range(counter):
        x += 1
    print('exit from addx\n')
    return

def subx():
    global x
    for i in range(counter):
        x -= 1
    print('exit from subx\n')
    return

t1 = threading.Thread(target=addx)
t2 = threading.Thread(target=subx)
t1.start()
t2.start()
t1.join()
t2.join()

print('value of x = ', x)
print('exit from main thread')

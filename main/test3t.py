from memory.memmgmt import MemoryManagement
from memory.memmgr import Memory
from process.processx import Process
import threading
import time
    

def printAll(astring, process):
    print(" ********* start: ", astring, '*********')
    process.print_mgmt()
    Memory.print_mem()
    MemoryManagement.print_management()
    print(" *********** end: ", astring, '***********')

# first process
def p1thread():
    p1 = Process(4)
    p1.load_pages([0,1], 2)
    printAll("first process p1 ", p1)
    p1.load_pages([2], 1)
    printAll("More memory added to p1 ", p1)

# second process
def p2thread():
    p2 = Process(3)
    p2.load_pages([0], 1)
    printAll("second process p2 ", p2)
    p2.load_pages([1], 1)
    printAll("More memory added to p2 ", p2)

# third process
def p3thread():
    p3 = Process(3)
    p3.load_pages([0,1], 2)
    printAll("third process p3 ", p3)

# forth process
def p4thread():
    p4 = Process(4)
    p4.load_pages([0,1], 2)
    printAll("forth process p4 ", p4)


t1 = threading.Thread(target=p1thread, args=())
t1.start()

t2 = threading.Thread(target=p2thread, args=())
t2.start()

t3 = threading.Thread(target=p3thread, args=())
t3.start()

t4 = threading.Thread(target=p4thread, args=())
t4.start()

print('End main thread')
import sys
sys.path.append('/Users/quentincurteman/Google Drive File Stream/My Drive/William Jessup/Fall 2018/Operating Systems/CS355')

from random import *

from memory.memmgmt import MemoryManagementA
from memory.memmgr import MemoryA
from process.processx import Process

def modify(px):
    nbr = px.get_my_pid()
    vectorlist = px.get_vectors()
    for v in vectorlist:
        for r in range(0,v.shape[0]):
            v[r] = nbr
    

def printAll(astring, process):
    print(" ********* start: ", astring, '*********')
    process.print_mgmt()
    MemoryA.print_mem()
    MemoryManagementA.print_management()
    print(" *********** end: ", astring, '***********')

def add_random_marks():
    for loop in range(25):
        index = randint(0, 6)
        MemoryManagementA.mark(index)

# first process
p1 = Process(4)
p1.load_pages([0,1], 2)
modify(p1)
printAll("first process p1 ", p1)

# second process
p2 = Process(3)
p2.load_pages([0], 1)
modify(p2)
printAll("second process p2 ", p2)

# first process does another load_pages
p1.load_pages([2],1)
modify(p1)
printAll(" first process p1 do a load again", p1)

# second process does another load
p2.load_pages([1],1)
modify(p2)
printAll(" second process p2 do a load again", p2)

# third process
p3 = Process(3)
p3.load_pages([0,1], 2)
modify(p3)
add_random_marks()
printAll("third process p3 ", p3)

# forth process
p4 = Process(4)
p4.load_pages([0,1,2], 3)
modify(p4)
printAll("forth process p4 ", p4)


'''
need to make new stuff:
- mark()
- unmark()
- sweep()
  - decrements mark_counter for each pageframe
'''
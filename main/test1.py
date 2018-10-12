import sys
sys.path.append('/Users/quentincurteman/Google Drive File Stream/My Drive/William Jessup/Fall 2018/Operating Systems/CS355')

from memory.memmgmt import MemoryManagement
from memory.memmgr import Memory
from process.processx import Process

p1 = Process(4)
p1.print_mgmt()

print(" ***** before loading ****")
Memory.print_mem()
MemoryManagement.print_management()
print(" ******************")

alist = [0,1]
p1.load_pages(alist, 2)

print(" ***** after loading ****")
p1.print_mgmt()
Memory.print_mem()
MemoryManagement.print_management()
print(" ******************")

# now get those vestors
vectorlist = p1.get_vectors()
nbr = 22
for v in vectorlist:
    for r in range(0,v.shape[0]):
        v[r] = nbr
    nbr += 11

print(" ***** modifying  ****")
Memory.print_mem()
print(" ******************")
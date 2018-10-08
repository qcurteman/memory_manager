
import numpy as np

class MemMgr:

    row_size = 10
    column_size = 6
    meme = np.empty(shape=(row_size, column_size), dtype='int8')

    @classmethod
    def get_mem(cls, pid, nbrblocks):
        print('get_mem from pid = ', pid, " for nbrBlocks = ",nbrblocks)
        aa = np.empty(shape=(10, 8), dtype='int8')
        return aa

    @classmethod
    def release_mem(cls, pid):
        print('release_mem from pid ', pid)
        return 456

    @classmethod
    def display_mem(cls):
        print('display memory')

    @classmethod
    def display_mgmt(cls):
        print('display management structures')

class Mem1:
    row_size = 10
    column_size = 6
    memaa = np.empty(shape=(row_size, column_size), dtype='int8')
    for i in range(len(memaa)):
        for j in range(len(memaa[i])):
            memaa[i][j] = 0
    
    mem_index = dict()
    for row in range(row_size):
        mem_index[row] = 0

    #index = 0
    #for i in range(len(memaa)):
    #    for j in range(len(memaa[i])):
    #        if index == 2 or index == 3 or index == 4:
    #            memaa[i][j] = 33

    #        if index == 0 or index == 1:
    #            memaa[i][j] = 111

    #        if index == 5 or index == 6 or index == 7:
    #            memaa[i][j] = 66
    #    index += 1

    @classmethod
    def insert_memory(cls, pid, nbrblocks):
        consecutive_space = 0
        start_index = None
        enough_space = False
        for index in range(len(Mem1.mem_index)):
            if Mem1.mem_index[index] == 0:
                start_index = index
                temp_index = start_index
                while temp_index < 10 and Mem1.mem_index[temp_index] == 0:
                    consecutive_space += 1
                    temp_index += 1
                if consecutive_space >= nbrblocks:
                    enough_space = True
                    for block_entry in range(nbrblocks):
                        for col in range(Mem1.memaa.shape[1]):
                            Mem1.mem_index[start_index] = pid
                            Mem1.memaa[start_index][col] = pid
                            start_index += 1

        if enough_space == False:
            raise Exception('Not enough space in memory.')        
        
        

    @classmethod
    def display_all(cls):
        print(Mem1.memaa)

    @classmethod
    def get_mem(cls, pid, nbrblocks):
        # nbrblocks is number of rows
        print('get_mem from pid = ', pid, " for nbrBlocks = ",nbrblocks)
        for row in range(Mem1.memaa.shape[0]):
            size_range = 0
            if Mem1.memaa[row][0] == pid:
                start = row
                break
            
        viewa = Mem1.memaa[start:start+nbrblocks,:6]
        return viewa

    @classmethod
    def release_mem(cls, pid):
        print('release_mem from pid ', pid)
        return 456

    @classmethod
    def display_mem(cls):
        print('display memory')
        print(Mem1.memaa)

    @classmethod
    def display_mgmt(cls):
        print('display management structures')
    

mm = Mem1()
mm.insert_memory(66, 3)
view = mm.get_mem(66, 3)
print(view)
mm.display_mem()

# change contents of my view
#rsize = aa1.shape[0]
#print('rsize: ', rsize)
#csize = aa1.shape[1]
#print('csize: ', csize)
#for r in range(0,rsize):
#    for c in range(0,csize):
#        aa1[r,c] = 55

#print('\n')
#print(aa1)
#print("parent")
#Mem1.display_all()


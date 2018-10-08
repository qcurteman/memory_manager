import numpy as np

import sys
sys.path.append('/Users/quentincurteman/Google Drive File Stream/My Drive/William Jessup/Fall 2018/Operating Systems/CS355')


from memory.memerror import MemoryError
from memory.memmgmt import MemoryManagementA

class MemoryA:

    # constants
    row_size = 7
    column_size = 5

    memory = np.zeros(shape=(row_size, column_size), dtype='int8')
    process_list = []

    @classmethod
    def get_mem(cls, pid, nbrPages):
        mem_list = []
        page_frame_indexes = MemoryManagementA.find_free_space(pid, nbrPages)
            # returns a list of pageFrames
            # if none, returns an empty list
        if len(page_frame_indexes) > 0:
            for pageFrameIndex in page_frame_indexes:
                vectora = MemoryA.memory[pageFrameIndex, :]
                tuplea = (pageFrameIndex, vectora) # vectora is a POINTER to memory
                mem_list.append(tuplea)
                MemoryA.update_processes(pageFrameIndex)
        return mem_list
    
    @classmethod
    def update_processes(cls, page_frame_index):
        for process in MemoryA.process_list:
            for index in range(len(process.page_table)):
                if page_frame_index == process.page_table[index]:
                    process.unsetx(page_frame_index) #TODO: fix

    @classmethod
    def modify_memory(cls, px):
        nbr = px.get_my_pid()
        vectorlist = px.get_vectors()
        for v in vectorlist:
            for r in range(len(v)):
                v[r] = nbr
        indexes_to_remove = MemoryA.check_process_list()
        MemoryA.remove_process(indexes_to_remove)


    @classmethod
    def check_process_list(cls):
        indexes_to_remove = []
        for index in range(len(MemoryA.process_list)):
            in_mem = False
            for row in range(len(MemoryA.memory)):
                if MemoryA.process_list[index].mypid == MemoryA.memory[row][0]:
                    in_mem = True
                    break
            if in_mem == False:
                indexes_to_remove.append(index)
            
        return indexes_to_remove
            

    @classmethod
    def register_process(cls, process):
        MemoryA.process_list.append(process)

    @classmethod
    def remove_process(cls, indexes_to_remove):
        for index in range(len(indexes_to_remove)):
            MemoryA.process_list.pop(indexes_to_remove[index])
        

    @classmethod
    def print_mem(cls, ):
        print('--------------- memory array ---------------')
        for r in range(0, MemoryA.row_size):
            print(r, ' : ', MemoryA.memory[r])
        print('--------------------------------------------')

        print('--------------- process list ---------------')
        for i in range(len(MemoryA.process_list)):
            print(i, ' : ', MemoryA.process_list[i].mypid)
        print('--------------------------------------------')
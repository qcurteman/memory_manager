import numpy as np
import threading
from memory.memerror import MemoryError
from memory.memmgmt import MemoryManagement

class Memory:

    # constants
    row_size = 7
    column_size = 5

    memory = np.zeros(shape=(row_size, column_size), dtype='int8')
    process_list = []

    lock = threading.RLock()

    @classmethod
    def get_mem(cls, pid, nbrPages):
        mem_list = []
        with Memory.lock:
            page_frame_indexes = MemoryManagement.find_free_space(pid, nbrPages)
            # returns a list of pageFrames
            # if none, returns an empty list
        if len(page_frame_indexes) > 0:
            for pageFrameIndex in page_frame_indexes:
                vectora = Memory.memory[pageFrameIndex, :]
                tuplea = (pageFrameIndex, vectora) # vectora is a POINTER to memory
                mem_list.append(tuplea)
                with Memory.lock:
                    Memory.update_processes(pageFrameIndex)
                    MemoryManagement.set_management(pageFrameIndex, pid)
        return mem_list
    
    @classmethod
    def update_processes(cls, page_frame_index):
        for process in Memory.process_list:
            for index in range(len(process.page_table)):
                if page_frame_index == process.page_table[index]:
                    process.unsetx(page_frame_index)

    @classmethod
    def modify_memory(cls, px):
        nbr = px.get_my_pid()
        vectorlist = px.get_vectors()
        for v in vectorlist:
            for r in range(len(v)):
                v[r] = nbr
        indexes_to_remove = Memory.check_process_list()
        Memory.remove_process(indexes_to_remove)


    @classmethod
    def check_process_list(cls):
        indexes_to_remove = []
        for index in range(len(Memory.process_list)):
            in_mem = False
            for row in range(len(Memory.memory)):
                if Memory.process_list[index].mypid == Memory.memory[row][0]:
                    in_mem = True
                    break
            if in_mem == False:
                indexes_to_remove.append(index)
            
        return indexes_to_remove
            

    @classmethod
    def register_process(cls, process):
        Memory.process_list.append(process)

    @classmethod
    def remove_process(cls, indexes_to_remove):
        for index in range(len(indexes_to_remove)):
            Memory.process_list.pop(indexes_to_remove[index])
        

    @classmethod
    def print_mem(cls, ):
        print('--------------- memory array ---------------')
        for r in range(0, Memory.row_size):
            print(r, ' : ', Memory.memory[r])
        print('--------------------------------------------')

        print('--------------- process list ---------------')
        for i in range(len(Memory.process_list)):
            print(i, ' : ', Memory.process_list[i].mypid)
        print('--------------------------------------------')
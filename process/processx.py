import numpy as np

import sys
sys.path.append('/Users/quentincurteman/Google Drive File Stream/My Drive/William Jessup/Fall 2018/Operating Systems/CS355')

from memory.memmgmt import MemoryManagementA
from memory.memmgr import MemoryA

class Process:
    pid_counter = 12

    def __init__(self, initialNbrOfPages):
        self.page_table = np.zeros(shape=(initialNbrOfPages, 1), dtype='int64')
        self.page_frame_vectors = [0] * initialNbrOfPages
        for i in range(self.page_table.shape[0]):
            self.page_table[i] = -1
        self.available_space = initialNbrOfPages
        self.mypid = Process.get_pid()
        MemoryA.register_process(self)

    def load_pages(self, listOfPages, nbrPages):
        listPageFrameVector = MemoryA.get_mem(self.mypid, nbrPages)
        for i in range(0, len(listOfPages)):
            pageFrameIndex, vectora = listPageFrameVector[i] # vectora is a pointer to memory
            self.setx(listOfPages[i], pageFrameIndex, vectora)

    def remove_page_frame(self, pageFrameIndex):
        for index in range(len(self.page_table)):
            if self.page_table[index] == pageFrameIndex:
                self.page_table[index] = -1
                self.page_frame_vectors[index] = -1

    def setx(self, page, pageFrameIndex, vectora): #change name later pls
        for i in range(self.page_table.shape[0]):
            if self.page_table[i][0] == -1:
                self.page_table[i][0] = pageFrameIndex
                self.page_frame_vectors[i] = vectora
                self.available_space += 1
                break
        MemoryA.modify_memory(self)

    def unsetx(self, pageFrameIndex):
        for index in range(len(self.page_table)):
            if self.page_table[index][0] ==  pageFrameIndex:
                self.page_table[index][0] = -1
                self.page_frame_vectors[index] = [0]
                self.available_space -= 1
                return
        raise(MemoryError('The page frame index that was attempted to be removed does not exist in this process.'))

    def get_vectors(self):
        temp_list = []
        for row in range(len(self.page_frame_vectors)):
            if type(self.page_frame_vectors[row]) != int:
                temp_list.append(self.page_frame_vectors[row])
        
        return temp_list

    def print_mgmt(self):
        for i in range(self.page_table.shape[0]):
            print('{}:    {}    {}'.format(i, self.page_table[i], self.page_frame_vectors[i]))

    def get_my_pid(self):
        return self.mypid

    @classmethod
    def get_pid(cls):
        aa = Process.pid_counter
        Process.pid_counter += 23
        return aa



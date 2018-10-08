import numpy as np
import time
from random import *

import sys
sys.path.append('/Users/quentincurteman/Google Drive File Stream/My Drive/William Jessup/Fall 2018/Operating Systems/CS355')


class MemoryManagementA:
    # constants
    row_size = 7
    column_size = 3

    management = np.zeros(shape=(row_size, column_size), dtype='double')

    @classmethod
    def find_free_space(cls, pid, nbrPages):
        alist = MemoryManagementA.find_existing(pid, nbrPages)
        num_frames_needed = nbrPages - len(alist)
        if num_frames_needed > 0:
            #blist = MemoryManagementA.first_in_first_out(pid, num_frames_needed)
            
            blist = MemoryManagementA.least_commonly_used(pid, num_frames_needed)
            

            alist += blist
        return alist

    @classmethod
    def find_existing(cls, pid, nbrPages):
        free_space_indexs = []
        enough_space = False
        for index in range(MemoryManagementA.row_size):
            if MemoryManagementA.management[index][0] == 0:
                free_space_indexs.append(index)
            if len(free_space_indexs) == nbrPages:
                enough_space = True
                break
        if enough_space:
            return free_space_indexs
        else:
            return []

    @classmethod
    def least_commonly_used(cls, pid, num_frames_needed):
        index_list = MemoryManagementA.get_low_val_list(pid, num_frames_needed, 2)
        MemoryManagementA.sweep()

        return index_list

    @classmethod
    def sweep(cls):
        for index in range(MemoryManagementA.row_size):
            if MemoryManagementA.management[index][2] > 0:
                MemoryManagementA.management[index][2] -= 1

    @classmethod
    def first_in_first_out(cls, pid, num_frames_needed):
        index_list = MemoryManagementA.get_low_val_list(pid, num_frames_needed, 1)
        
        return index_list

    @classmethod
    def get_low_val_list(cls, pid, num_frames_needed, col_to_compare):
        
        def getLowestNum(index_list):
            for index in range(MemoryManagementA.management.shape[0]):
                if index not in index_list:
                    return MemoryManagementA.management[index][1], index
            raise(MemoryError('Not enough space in memory for new process.'))

        index_list = []
        for loop_num in range(num_frames_needed):
            lowest_num, lowest_index = getLowestNum(index_list)
            for index in range(MemoryManagementA.management.shape[0]):
                if index in index_list:
                    continue
                elif MemoryManagementA.management[index][col_to_compare] < lowest_num:
                    lowest_num = MemoryManagementA.management[index][col_to_compare]
                    lowest_index = index
            index_list.append(lowest_index)
        return index_list


    @classmethod
    def set_management(cls, pageFrameIndex, pid): # change name pls
        MemoryManagementA.management[pageFrameIndex][0] = pid
        MemoryManagementA.management[pageFrameIndex][1] = time.time()
        MemoryManagementA.management[pageFrameIndex][2] = 0
        MemoryManagementA.mark(pageFrameIndex)

    @classmethod
    def remove_management(cls, pageFrameIndex): 
        #remove the pid cell to zero
        MemoryManagementA.management[pageFrameIndex][0] = 0
        MemoryManagementA.management[pageFrameIndex][1] = 0


    @classmethod
    def mark(cls, pageFrameIndex):
        MemoryManagementA.management[pageFrameIndex][2] += 1

    @classmethod
    def print_management(cls, ):
        print('------------- management array -------------')
        for r in range(0, MemoryManagementA.row_size):
            print(r, ' : ', int(MemoryManagementA.management[r][0]), ', ', MemoryManagementA.management[r][1], ', ', 
            MemoryManagementA.management[r][2])
        print('--------------------------------------------')

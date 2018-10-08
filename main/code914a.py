import numpy as np
import traceback

row_size = 6
col_size = 6
my_array = np.zeros(shape=(row_size, col_size), dtype='int8')

viewa = my_array[0:2]
for i in range(0,1):
    for j in range(col_size):
        viewa[i,j] = 22

for i in range(1,2):
    for j in range(col_size):
        viewa[i,j] = 44

np.save('view-a.npy', viewa)

viewb = my_array[2:5]
for i in range(2,3):
    for j in range(col_size):
        viewb[i,j] = 33

temp = np.load('view-a.npy')

for i in range(len(temp)):
    viewb[i] = temp[i]

print('viewb:\n', viewb)
print('my_array:\n', my_array)

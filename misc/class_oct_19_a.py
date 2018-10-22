import multiprocessing as mp

context = mp.get_context('spawn')
result_queue = context.Queue()
run_queue = context.Queue()

def consumer1(arr):

    def square(arr):
        temp = list()

        for i in range(4):
            temp.append(arr[i] * arr[i])
        #print(temp)
        return temp

    temp_arr = square(arr)
    result_queue.put((temp_arr, 'squared'))

def consumer2(arr):

    def cube(arr):
        temp = list()
        for i in range(4):
            temp.append(arr[i] * arr[i] * arr[i])
        #print(temp)
        return temp

    temp_arr = cube(arr)
    result_queue.put((temp_arr, 'cubed'))

def Parent(arr_list):
    for item in arr_list:
        run_queue.put(item)
    

    p1 = mp.Process(target=consumer1, args=(run_queue.get(),))
    p2 = mp.Process(target=consumer2, args=(run_queue.get(),))
    p1.start()
    p2.start()

    print(result_queue.get())
    print(result_queue.get())
    



if __name__ == '__main__':
    arr_list = [[1,2,3,4],[1,2,3,4]]

    p = mp.Process(target=Parent, args=(arr_list,))
    p.start()
    p.join()
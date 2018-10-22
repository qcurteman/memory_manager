import multiprocessing as mp
import time as time


def foo(q):
    q.put('hello')
    q.put([42, None, 'hello'])
    time.sleep(5)
    q.put('Quentin was here')
    

if __name__ == '__main__':
    context = mp.get_context('spawn')
    q = context.Queue()
    p = context.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    print(q.get())
    print('waiting for third get')
    print(q.get())


    p.join()
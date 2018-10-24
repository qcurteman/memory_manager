import multiprocessing as mp

to_dispatcher_queue = context.Queue()

class Dispatcher(mp.Process):
    def __init__(self):
        self.input_queue = context.Queue()
        self.output_queue = context.Queue()
    
    def run(self):
        while True:
            if not self.input_queue.empty():
                self.dispatch_process(self.input_queue.get())

            if not to_dispatcher_queue.empty():
                self.output_queue.put(to_dispatcher_queue.get())
            
    def dispatch_process(self, input_list):
        # if even 


class Worker(mp.Process):
    def __init__(self,):
        self.my_queue = context.Queue()
    
    def run():
        while True:


    def even_process(input_list):
        # send result to "to_dispatcher_queue"

    def odd_process(input_list):
        # send result to "to_dispatcher_queue"

class Controller():
    def __init__(self):
        even2 = Worker()
        even3 = Worker()
        even4 = Worker()
        even5 = Worker()

    def send_to_dispatcher(self,):
        

    
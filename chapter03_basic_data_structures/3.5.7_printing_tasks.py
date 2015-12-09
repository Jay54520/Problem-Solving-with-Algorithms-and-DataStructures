from queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.ppm = ppm
        self.current_task = None
        self.time_remaining = 0
        
    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None 
                
    def is_busy(self):
        if self.current_task != None:
            return True 
        else:
            return False 
            
    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() / self.ppm * 60
        
class Task:
    def __init__(self, start_time):
        self.start_time = start_time
        self.pages = random.randrange(1, 21)
        
    def get_pages(self):
        return self.pages 
        
    def wait_time(self, current_time):
        return current_time - self.start_time 
        
def simulation(num=10, ppm=10, hours=1):
    q = Queue()
    p = Printer(ppm)
    waiting_times = []
    
    for current_second in range(0, hours*3600):
        if new_print_task(num):
            task = Task(current_second)
            q.enqueue(task)
            
        if not p.is_busy() and not q.is_empty():
            task = q.dequeue()
            # start_time 是在 上一个 if 中添加，现在轮到进入打印机
            # 等待终止
            waiting_times.append(task.wait_time(current_second))
            p.start_next(task)
        
        p.tick()
        
    average_wait = sum(waiting_times) / len(waiting_times)
    
    print("Average wait %6.2f secs %3d tasks remaining."
        % (average_wait, q.size()))

def new_print_task(num):
    if random.randrange(1800 // num)  == 1:
        return True 
    else:
        return False 
        
for i in range(10):
    simulation()
    

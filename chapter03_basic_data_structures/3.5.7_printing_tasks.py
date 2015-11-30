from queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
        
    def tick(self):
        if self.current_task != None:
            # 现在求得是每秒钟的打印 for current_second in num_seconds
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None
                
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False 
            
    def start_next(self, new_task):
        self.current_task = new_task
        # 模拟打印时间 秒
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate
 
class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
        
    def get_stamp(self):
        return  self.timestamp
        
    def get_pages(self):
        return self.pages
        
    def wait_time(self, current_time):
        return current_time - self.timestamp
        
def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []
    
    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)
            
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            # 与 pages_per_minute 有没有关？ 这里怎么计算的秒数，我又没有经过那么长时间
            # 有关。 time_remaining -= 1 初始 time_remaining = new_task.get_pages() * 60 / self.page_rate
            # 我自己加上 当前的 打印时间 ，书上没加
            waiting_times.append(next_task.wait_time(current_second)+next_task.get_pages()/pages_per_minute*60)
            lab_printer.start_next(next_task)
        
        # 减去当前时间 1s 在 Printer 类z中通过剩余时间判断是否为空闲 
        lab_printer.tick()
    
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining."
        % (average_wait, print_queue.size()))
            
def new_print_task():
    if random.randrange(1, 181) == 180:
        return True
    else:
        return False
        
for i in range(10):
    simulation(3600, 5)
        
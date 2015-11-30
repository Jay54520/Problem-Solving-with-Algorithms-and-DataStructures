from queue import Queue
import random

class Printer():
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
        
    # 开始打印 每秒钟
    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1;
            # 如果打印完了， 就是剩余时间 < 0，打印机变为空闲
            if self.time_remaining < 0:
                self.current_task = None
            
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
            
    def start_next(self, new_task):
        self.current_task = new_task
        # 模拟打印时间 秒
        self.time_remaining = new_task.get_pages()/self.page_rate*60
        return self.time_remaining
    
class Task():
    def __init__(self, current_second):
        self.timestamp = current_second
        self.pages = random.randint(1, 20)
        
    def get_pages(self):
        return self.pages
        
    def wait_time(self, current_time):
        return current_time - self.timestamp
    
def simulation(num_seconds, num_students, pages_per_minute):
    print_queue = Queue()
    lab_printer = Printer(pages_per_minute)
    waiting_times = []
    
    for current_second in range(num_seconds):
        if new_print_task(num_students):
            # 创建一个任务
            task = Task(current_second)
            print_queue.enqueue(task)
        
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            lab_printer.start_next(next_task)
            # 等待上一个的时间 + 自己打印所需时间
            waiting_times.append(next_task.wait_time(current_second) + 
                next_task.get_pages() / pages_per_minute * 60)
            
        # 打印机过去1秒钟
        lab_printer.tick()
        
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average wait %6.2f secs %3d remaining" % (average_wait, print_queue.size()))
    
def new_print_task(num_students):
    chance = 1800 // num_students
    if random.randrange(1, chance+1) == 1:
        return True
    else:
        return False

for i in range(10):
    simulation(3600, 10, 10)        
        
        
        
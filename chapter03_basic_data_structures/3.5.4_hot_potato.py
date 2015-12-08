from queue import Queue
import random

def hot_potato(name_list):
    a_queue = Queue()
    for name in name_list:
        a_queue.enqueue(name)
        
    while a_queue.size() > 1:       
        num = random.randint(1, 7)
        for i in range(num):
            tem = a_queue.dequeue()
            a_queue.enqueue(tem)
        a_queue.dequeue()
            
    return a_queue.dequeue()
    
print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent",
    "Brad"]))    
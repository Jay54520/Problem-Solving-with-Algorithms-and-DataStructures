from queue import Queue

def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
            
        # 传了 num 次数后，排除有 potato 的那个人
        sim_queue.dequeue()
        
    return sim_queue.dequeue()
    
print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent",
    "Brad"], 7))    
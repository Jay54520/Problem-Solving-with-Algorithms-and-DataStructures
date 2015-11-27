import time
def find_minimum(list):
    start = time.time()
    global minimum
    minimum = list[0]
    for num in list:
        if num < minimum:
            minimum = num 
    end = time.time()
    return minimum, end-start 
    
for i in range(5):
    print(find_minimum(list(range(1000000))))
    
    
        
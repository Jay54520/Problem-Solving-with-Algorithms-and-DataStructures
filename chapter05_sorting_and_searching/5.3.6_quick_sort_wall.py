import ipdb

# https://www.youtube.com/watch?v=aQiWF4E8flQ
# 这个还是错误的
def quick_sort(a_list):
    length = len(a_list)
    wall = 0
    pivot = length - 1
    #ipdb.set_trace()
    while wall != length - 1:
        for current in range(0, length):        
            if a_list[current] < a_list[pivot]:
                print(current, '<-->', wall)
                a_list[current], a_list[wall] = a_list[wall], a_list[current]
                wall += 1
            # swap pivot and current wall            
        a_list[wall], a_list[pivot] = a_list[pivot], a_list[wall]
    
    return a_list
    
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)    
        
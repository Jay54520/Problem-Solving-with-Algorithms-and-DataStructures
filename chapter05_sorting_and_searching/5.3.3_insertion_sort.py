def insertion_sort(a_list):    
    # 假定 a_list[0] 是一个有序序列
    for num in range(1, len(a_list)):
        while num - 1 >= 0:         
            if a_list[num] < a_list[num - 1]:                
                a_list[num], a_list[num - 1] = a_list[num - 1], a_list[num]
            num -= 1
    
    return a_list
    
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)
            
            
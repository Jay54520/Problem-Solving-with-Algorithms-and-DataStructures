def selection_sort(a_list):
    # range 左闭右开
    for num in range(len(a_list) - 1, -1, -1):
        pos_of_max = 0
        for sub_num in range(0, num +1):
            if a_list[sub_num] > a_list[pos_of_max]:
                pos_of_max = sub_num
        # 找出最大的位置，再交换一次
        a_list[pos_of_max], a_list[sub_num] = a_list[sub_num], a_list[pos_of_max]
    
    return  a_list
    
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list) 
            
        
        
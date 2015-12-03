def merge_sort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_list = [a_list[x] for x in range(0, mid)]
        right_list = [a_list[x] for x in range(mid, len(a_list))]
        
        merge_sort(left_list)
        merge_sort(right_list)
        
        # Merging
        left_num = 0
        right_num = 0
        num = 0
        
        # 当两个数组都不为空
        while left_num < len(left_list) and right_num < len(right_list):
            if left_list[left_num] < right_list[right_num]:
                a_list[num] = left_list[left_num]
                left_num += 1
            else:
                a_list[num] = right_list[right_num]
                right_num += 1
            num += 1
            
        # right_list 为空，left_list 中是排好序的，最小的大于 a_list 中是排好序的，最小的大于
        # 所以只需要把 left_list 中按顺序加入 a_list
        while left_num < len(left_list):
            a_list[num] = left_list[left_num]
            left_num += 1
            num += 1
            
        while right_num < len(right_list):
            a_list[num] = right_list[right_num]
            right_num += 1
            num += 1
    print("Merging ", a_list)
    
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)    
        
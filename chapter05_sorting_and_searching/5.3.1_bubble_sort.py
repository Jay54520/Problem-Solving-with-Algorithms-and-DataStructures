def bubble_sort(a_list):
    length = len(a_list)
    pairs = length - 1
    exchanges = True
    
    while pairs > 1 and exchanges:
        # 如果下面没有变动，则说明已经排序完毕
        exchanges = False
        for element in range(pairs):
            if a_list[element] > a_list[element+1]:
                exchanges = True
                # simultaneous 减少占用空间
                a_list[element], a_list[element+1] = a_list[element+1], a_list[element]                
        pairs -= 1    
    return a_list
    
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)    
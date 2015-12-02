def bubble_sort(a_list):
    length = len(a_list)
    pairs = length - 1
    
    while pairs > 1:
        for element in range(pairs):
            if a_list[element] > a_list[element+1]:
                temp = a_list[element]
                a_list[element] = a_list[element+1]
                a_list[element+1] = temp
        pairs -= 1    
    return a_list
    
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)    
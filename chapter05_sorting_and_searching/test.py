def binary_search(a_ascending_list, num):
    first = 0
    last = len(a_ascending_list) - 1
    found = False 
    
    while first <= last and not found:
        mid = (first + last) // 2
        if a_ascending_list[mid] == num:
            found = True
        else:
            if a_ascending_list[mid] > num:
                last = mid - 1
            else:
                first = mid + 1 
                
    return found
    
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))    

def binary_search_wrong(a_ascending_list, num):    
    found = False
    half = len(a_ascending_list) // 2
    while len(a_ascending_list) > 1 and not found:
        if a_ascending_list[half] == num:
            found = True
        elif a_ascending_list[half] < num:
            binary_search(a_ascending_list[half + 1:], num)
        else:
            binary_search(a_ascending_list[:half], num)
        
    if len(a_ascending_list) == 1:
        if a_ascending_list[0] == num:
            return True
        else:
            return False
    
    return found
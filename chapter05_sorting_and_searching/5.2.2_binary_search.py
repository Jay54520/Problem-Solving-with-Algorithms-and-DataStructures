def binary_search(order_list, search_num):
    first = 0
    last = len(order_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if order_list[midpoint] == search_num:
            found = True
        else:
            if order_list[midpoint] > search_num:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    return found

def binary_search_recursive(order_list, search_num):
    if len(order_list) == 0:
        return False
    else:
        midpoint = len(order_list) // 2 
        if order_list[midpoint] == search_num:
            return True
        elif order_list[midpoint] > search_num:
            # 递归引用不能少了 return 
            return binary_search_recursive(order_list[:midpoint - 1], search_num)
        else:
            return binary_search_recursive(order_list[midpoint + 1:], search_num)
    
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))    

print(binary_search_recursive(test_list, 3))
print(binary_search_recursive(test_list, 13))
        
        
    
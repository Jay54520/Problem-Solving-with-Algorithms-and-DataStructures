def quick_sort(array=[54, 26, 93, 17, 77, 31, 44, 55, 20]):
    less = []
    equal = []
    greater = []
    
    if len(array) > 1:
        pivot = array[0]
        for element in array:
            if element < pivot:
                less.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                greater.append(element)
        
        return quick_sort(less) + quick_sort(equal) + quick_sort(greater)   
    # 只有一个元素就返回该序列
    else:
        return array
        
print(quick_sort())

def quick_sort_improve(array=[54, 26, 93, 17, 77, 31, 44, 55, 20]):        
    if len(array) > 1:
        pivot = array[0]
        # 将 append 变为　[x for x in [] if ]
        return quick_sort_improve([x for x in array if x < array[0]]) + [array[0]] + \
            quick_sort_improve([x for x in array if x > array[0]])
    # 只有一个元素就返回该序列
    else:
        return array
        
print(quick_sort_improve())
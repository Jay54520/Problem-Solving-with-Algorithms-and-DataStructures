import random
import timeit
import ipdb
"""
Given array A of size n and integer k ≤ n,
1. Pick a pivot element p at random from A.
2. Split A into subarrays LESS and GREATER by comparing each element to p as in Quicksort. While we are at it, count the number L of elements going in to LESS.
3. (a) If L = k − 1, then output p.
(b) If L > k − 1, output QuickSelect(LESS, k).
(c) If L < k − 1, output QuickSelect(GREATER, k − L − 1)
"""
def quick_select(a_list, k):        
    a_list_length = len(a_list)       
    pivot = a_list[random.randint(0, a_list_length - 1)]    
    less = [num for num in a_list if num < pivot]
    greater = [num for num in a_list if num > pivot]
    less_length = len(less)
    # 如果比 k 小的数字有 k - 1 个， 则 pivot 就是第 k 小的数字
    if less_length == k - 1:           
        return pivot
    # 如果比 k 小的数字不足 k - 1 个，则 pivot 在 第 k　小的数字的左边，
    # 我们就要在右边大于 pivot 的 list 中寻找
    if less_length < k - 1:          # k - 比 pivot 小的 减去 pivot 就是 k 所在的第几小
        return quick_select(greater, k - less_length - 1)
    if less_length > k - 1:
        return quick_select(less, k )

t = timeit.Timer('quick_select(a_list, 4)', 'from __main__ import quick_select, a_list')        
a_list = [5,33,6,2,4,7,8,9,12,41,25,64,57,86,79,1]
for i in range(10000, 1000000, 20000):
    print(quick_select(a_list, 4), "time for "+str(i)+":", t.timeit(i))
        
    
    
    
    
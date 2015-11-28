def angram_solution1(str1, str2):
    a_list = list(str2)
    pos1 = 0
    still_ok = True    
    while pos1 < len(str1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if str1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 += 1
        # 找完了 str2 还是没有找到
        if not found:
            still_ok = False
        # 找到了相同的，则继续找下一个，并且把 a_list 中找到的替换点掉
        else:
            pos1 += 1
            a_list[pos2] = None
    return still_ok
    
print(angram_solution1('abcd', 'dcba'))   

# 先排序，再比较
def angram_solution2(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    
    pos = 0
    match = True
    
    while pos < len(list1) and match:
        if list1[pos] == list2[pos]:
            match = True
            pos += 1
        else:
            match = False
            
    return match 

print(angram_solution1('abcd', 'dcba'))
   
# angram_solution3 generate all possibilities, compare   
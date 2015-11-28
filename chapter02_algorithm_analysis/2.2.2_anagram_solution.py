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
            
            
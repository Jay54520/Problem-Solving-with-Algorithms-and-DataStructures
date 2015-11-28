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

# ord() Given a string representing one Unicode character, 
# return an integer representing the Unicode code point of that character.

# Count with 26 characters and compare
def angram_solution4(str1, str2):
    # 26 个字母每个出现的次数，　list[index] 用 ord(pos) - ord('a') 表示
    list1 = [0] * 26
    list2 = [0] * 26
    
    # 计算字母出现的次数
    for character in str1:
        pos = ord(character) - ord('a')
        list1[pos] += 1
        
    for character in str2:
        pos = ord(character) - ord('a')
        list2[pos] += 1 

    # 判断两个 list 是否相等
    # 这里使用 while j < 26 比使用 for 迭代 list1 要好
    j = 0
    match = True
    while j < 26 and match:
        if list1[j] == list2[j]:
            match = True
            j += 1
        else:
            match = False
            
    return match 
    
    # 使用 for 迭代  O(n)
    # for i in range(list1):
        # if list1[i] == list2[i]:
            # match = True
        # else:
            # match = False 
            # break        

print(angram_solution4('abcd', 'dcba'))            
    
    
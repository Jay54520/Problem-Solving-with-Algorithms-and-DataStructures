def to_str(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        # base 转换需要翻过来 比如 stack
        return to_str(n // base, base) + convert_string[n % base]
        
print(to_str(1453, 16))        

from stack import Stack


# python 怎样处理 递归
def to_str2(n, base):
    r_stack = Stack()
    convert_string = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    
    res = ""
    while not r_stack.is_empty():
        res = res + r_stack.pop()
    return res
    
print(to_str2(1453, 16))
            
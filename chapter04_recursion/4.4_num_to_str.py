def to_str(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        # base 转换需要翻过来 比如 stack
        return to_str(n // base, base) + convert_string[n % base]
        
print(to_str(1453, 16))        
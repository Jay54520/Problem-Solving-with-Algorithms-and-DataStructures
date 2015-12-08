from stack import Stack
import ipdb

def base_converter(n, base=2):
    s = Stack()
    remainders = '0123456789ABCDEF'
    
    while n > 0:
        remainder = remainders[n % base]
        s.push(remainder)
        n = n // base 
        
    result = ""
    while not s.is_empty():
        result += str(s.pop())
    
    return result 
    
print(base_converter(42))
print(base_converter(256, 16))    
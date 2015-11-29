from stack import Stack
import ipdb

def base_converter(decimal_number, base=2):
    # 余数作为 index 与这个相对应 
    digits = '0123456789ABCDEF'
    reminder_stack = Stack()
    while decimal_number > 0:
        reminder = decimal_number % base
        reminder_stack.push(reminder)
        decimal_number = decimal_number // base
    
    # 将 reminder_stack 转化为 string
    new_string = ""
    while not reminder_stack.is_empty():
        new_string = new_string + digits[reminder_stack.pop()]
    
    return new_string
    
print(base_converter(42))
print(base_converter(25, 16))
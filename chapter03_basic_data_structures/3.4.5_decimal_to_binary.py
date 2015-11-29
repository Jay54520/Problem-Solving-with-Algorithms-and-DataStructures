from stack import Stack
import ipdb

def devide_by_2(decimal_number):
    reminder_stack = Stack()
    while decimal_number > 0:
        reminder = decimal_number % 2
        reminder_stack.push(reminder)
        decimal_number = decimal_number // 2
    
    # 将 reminder_stack 转化为 string
    binary_string = ""
    while not reminder_stack.is_empty():
        binary_string = binary_string + str(reminder_stack.pop())
    
    return binary_string
    
print(devide_by_2(42))
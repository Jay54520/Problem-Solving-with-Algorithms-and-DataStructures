from stack import Stack

# 括号之间匹配 后进先出 '(() () ())', '(((())))'
def par_checker(symbol_string):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbol_string) and balanced:
        if symbol_string[index] == '(':
            s.push(symbol_string[index])
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1
        
    if s == [] and balanced:
        return True
    else:
        return False
        
print(par_checker('(() () ())'))        
print(par_checker('(() () ('))
    
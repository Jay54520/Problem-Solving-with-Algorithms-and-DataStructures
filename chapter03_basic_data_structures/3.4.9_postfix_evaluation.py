from stack import Stack
import ipdb

def postfix_eval(postfix_string):
    s = Stack()
    postfix_list = postfix_string.split()
    
    for e in postfix_list:
        if e in '0123456789':
            s.push(e)
        else:
            right = int(s.pop())
            left = int(s.pop())
            s.push(do_math(e, left, right))
    
    return s.pop()
    
def do_math(op, op1, op2):
    if op == '+':
        return op1 + op2 
    elif op == '-':
        return op1 - op2 
    elif op == '*':
        return op1 * op2 
    else:
        return op1 / op2 
        
print(postfix_eval('7 8 + 3 2 + /'))          
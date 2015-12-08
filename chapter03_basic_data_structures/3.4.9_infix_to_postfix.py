from stack import Stack
import ipdb

def infix_to_postfix(infix_string):
    infix_list = infix_string.split()
    s = Stack()
    output = []
    p = {'(':0, ')':0, '+':1, '-':1, '*':2, '/':2, '^':3}
        
    for e in infix_list:
        if e in 'ABCDEFGHIJKLMNOPQRST' or e in '0123456789':
            output.append(e)
        elif e == '(':
            s.push(e)
        elif e == ')':
            while not s.peek() == '(':
                output.append(s.pop())
            s.pop()
        else:
            if not s.is_empty() and p[e] <= p[s.peek()]:                
                    output.append(s.pop())
            s.push(e)
    
    while not s.is_empty():
        output.append(s.pop())
        
    return " ".join(output)
        
    return result 
    
print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))    
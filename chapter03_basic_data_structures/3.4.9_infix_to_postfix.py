from stack import Stack
import ipdb

def infix_to_postfix(infix_string):
    infix_list = infix_string.split()
    s = Stack()
    output = []
    p = {'(':0, ')':0, '+':1, '-':1, '*':2, '/':2}
        
    for e in infix_list:
        if e in 'ABCDEFGHIJKLMNOPQRST' or e in '012346789':
            output.append(e)
        elif e == '(':
            s.push(e)
        elif e == ')':
            while not s.peek() == '(':
                output.append(s.pop())
            s.pop()
        else:
            if not s.is_empty():
                if p[e] <= p[s.peek()]:
                    output.append(s.pop())
            s.push(e)
    
    while not s.is_empty():
        output.append(s.pop())
        
    result = ""
    for e in output:
        result += e 
        
    return result 
    
print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B + C ) * C - ( D - E ) * ( F + G )"))    
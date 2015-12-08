from stack import Stack
import ipdb

def check_par(symbol_string):
    s = Stack()
    for a_symbol in symbol_string:
        if a_symbol in '{[(':
            s.push(a_symbol)
        elif a_symbol in '}])':
            if s.is_empty():
                return False 
            if not match(s.pop(), a_symbol):
                return False
    
    if not s.is_empty():
        return False 
        
    return True 
    
def match(open, close):
    opens = '{[('
    closes = '}])'
    
    return opens.index(open) == closes.index(close)
    
print(check_par('[[{{(())}}]]'))        
print(check_par('([)]'))    
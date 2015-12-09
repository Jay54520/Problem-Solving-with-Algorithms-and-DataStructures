from deque import Deque

def pal_checker(a_string):
    char_deque = Deque()
    
    for ch in a_string:
        char_deque.add_front(ch)
    
    match = True
    while char_deque.size() > 1 and match:
        if char_deque.remove_front() != char_deque.remove_rear():
            match = False 
    
    return match
    
print(pal_checker('maddam'))
print(pal_checker('abcd'))
from stack import Stack
import ipdb

# 括号类型是否匹配
def match(open, close):
    opens = '([{'
    closes = ')]}'
    # 返回 bool 值，直接　return 不需要再判断
    return opens.index(open) == closes.index(close)
    
# 括号之间匹配 后进先出 '[[{{(())}}]]', 不匹配的'([)]'，所以还需要加上类型匹配
def par_checker(symbol_string):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbol_string) and balanced:
        if symbol_string[index] in '([{':
            s.push(symbol_string[index])
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop() # 弹出上一个储存的 '([{' 中的一个
                if not match(top, symbol_string[index]):
                    balanced = False
        index += 1
        
    if s.is_empty() and balanced:
        return True
    else:
        return False
        
print(par_checker('[[{{(())}}]]'))        
print(par_checker('([)]'))
    
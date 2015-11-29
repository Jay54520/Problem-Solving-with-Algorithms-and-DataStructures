from stack import Stack
def infix_to_postfix(infix_expression):
    token_list = infix_expression.split()
    precedence = {}
    precedence["("] = 1
    precedence["+"] = 2
    precedence["-"] = 2
    precedence["*"] = 3
    precedence["/"] = 3
    operator_stack = Stack()
    postfix_list = []
    
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or \
            token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            # 弹出最后传入的 token 
            top_token = operator_stack.pop()
            while top_token != '(':
                # 这样括号里没有优先级比较                
                postfix_list.append(top_token)
                top_token = operator_stack.pop()
        # 比较 + - * / 优先级
        else:
            while (not operator_stack.is_empty()) and \
                (precedence[operator_stack.peek()] >= precedence[token]):
                postfix_list.append(operator_stack.pop())
            operator_stack.push(token)
        
    while not operator_stack.is_empty():
        postfix_list.append(operator_stack.pop())
    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B + C ) * C - ( D - E ) * ( F + G )"))
            
        
from stack import Stack

def postfix_evalution(postfix_expression):
    postfix_list = postfix_expression.split()
    stack = Stack()
    for token in postfix_list:        
        if token in '+-*/':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = do_math(token, operand1, operand2)
            stack.push(result)
        else:
            # 将 'number' 转化成数字
            token = int(token)
            stack.push(token)
    return stack.pop()
    
def do_math(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
        
print(postfix_evalution('7 8 + 3 2 + /'))        
    
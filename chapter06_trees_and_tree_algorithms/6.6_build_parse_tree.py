from stack import Stack 
from binarytree import BinaryTree

def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree 
    
    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            
            # p_stack 中的作为 parent, current_tree 指向
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        # operands 
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent 
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree 
    
pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
pt.postorder()

import operator 
def evaluate(parse_tree):
    opers = {"+": operator.add, '-': operator.sub, '*': operator.mul,
        '/': operator.truediv}
    
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()
    
    if left and right:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left), evaluate(right))
    else:
        return parse_tree.get_root_val()
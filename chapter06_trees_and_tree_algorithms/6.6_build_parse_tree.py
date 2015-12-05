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

def postorder_evaluate(tree):
    opers = {"+": operator.add, '-': operator.sub, '*': operator.mul,
        '/': operator.truediv}
    res1 = None    
    res2 = None    
    
    if tree:
        res1 = postorder_evaluate(tree.get_left_child())
        res2 = postorder_evaluate(tree.get_right_child())
        # 如果都是数字
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        # 如果到了 '叶子'
        else:
            return tree.get_root_val()
            
def print_exp(tree):
    str_val = ""
    if tree:
        str_val = '(' + print_exp(tree.get_left_child())
        str_val = str_val + str(tree.get_root_val())
        str_val = str_val + print_exp(tree.get_right_child()) + ')'
    return str_val
    
pt = build_parse_tree("( ( 10 + 5 ) * ( 2 + 2 ) )")
print(postorder_evaluate(pt))     
print(print_exp(pt))
        
def preorder(tree):
    if tree:
        print(tree.get_root_val)
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())
        
def postorder(tree):
    if tree:
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())
        print(tree.get_root_val())
        
def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())
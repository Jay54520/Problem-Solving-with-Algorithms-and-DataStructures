from stack import Stack 
from binarytree import BinaryTree

def build_parse_tree(exp):
    lst = exp.split()
    s = Stack()
    a_tree = BinaryTree('')
    # ？
    s.push(a_tree)
    cur = a_tree
    for i in lst:
        if i == '(':
            cur.insert_left(BinaryTree(''))
            s.push(cur)
            cur = cur.get_left_child()
        elif i not in '+-*/)':
            cur.set_root_val(i)
            parent = s.pop()
            cur = parent 
        elif i in '+-*/':
            cur.set_root_val(i)
            cur.insert_right(BinaryTree(''))
            s.push(cur)
            cur = cur.get_right_child()
        elif i == ')':
            parent = s.pop()
            cur = parent 
        else:
            return ValueError
    return a_tree 
    
pt = build_parse_tree("( ( 10 + 5 ) * 3 )")

import operator
def evaluate(tree)            :
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, 
            '/':operator.truediv}
    
    left_child = tree.get_left_child()
    right_child = tree.get_right_child()
    
    if left_child == None:
        return int(tree.get_root_val())
    else:
        fn = opers[tree.get_root_val()]
        return fn(evaluate(left_child), evaluate(right_child))
        
print(evaluate(pt))

def postorder_eval(tree)        :
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, 
            '/':operator.truediv}
    
    if tree != None:
        res1 = postorder_eval(tree.get_left_child())
        res2 = postorder_eval(tree.get_right_child())
        
        if res1 and res2:
            fn = opers[tree.get_root_val()]
            return fn(res1, res2)
        else:
            return int(tree.get_root_val())
            
print(postorder_eval(pt))

def inorder_exp(tree):
    str_val = ""
    if tree:
        if tree.get_left_child():
            str_val = '(' + inorder_exp(tree.get_left_child())
        else:
            str_val = inorder_exp(tree.get_left_child())
        str_val = str_val + tree.get_root_val()
        if tree.get_left_child():
            str_val = str_val + inorder_exp(tree.get_right_child()) + ')'
        else:
            str_val = str_val + inorder_exp(tree.get_right_child())
        
    return str_val
    
print(inorder_exp(pt))
    
    
          
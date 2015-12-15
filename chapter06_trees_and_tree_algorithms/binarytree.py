import ipdb
class Node:
    def __init__(self, value):
        self.value = value 
        self.parent = None
        self.left_child = None
        self.right_child = None 
        
    def insert(self, data):
        # 不需要重复的
        if self.value == data:
            return False 
        elif self.value > data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                self.left_child.parent = self
        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                self.right_child.parent = self
    
    def find(self, data):
        if self.value == data:
            return True 
        elif self.value > data:
            if self.left_child:
                self.left_child.find(data)
            else:
                return False 
        else:
            if self.right_child:
                self.right_child.find(data)
            else:
                return False
    
    # helper functions in delete 
    def is_left_child(self):
        return self.parent and self.parent.left_child == self 
    
    def is_right_child(self):
        return self.parent and self.parent.right_child == self         
        
    def has_both_child(self):
        return self.left_child and self.right_child
        
    def replace_node(self, *, value, left_child, right_child, parent):
        self.value = value 
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent 
        
    def find_successor(self):        
        if not self.left_child:
            return self
        else:
            self.left_child.find_successor()
            
    
    def delete(self, data):
        if self.value == data:
            # no child 
            if (not self.left_child) and (not self.right_child):                                                      
                if self.is_left_child():
                    self.parent.left_child = None                  
                elif self.is_right_child():
                    self.parent.right_child = None                  
                # the root and left, right need to delete the value 
                self = None            
            # two children
            elif self.has_both_child():
                ipdb.set_trace()
                succ = self.right_child.find_successor()
                self.value = succ.value 
                # delete succ 
                # no child 
                if (not succ.left_child) and (not succ.right_child):                                                      
                    if succ.is_left_child():
                        succ.parent.left_child = None                  
                    elif succ.is_right_child():
                        succ.parent.right_child = None
                # one child 只存在右子树
                else:
                    if succ.is_left_child():                        
                        succ.parent.left_child = succ.right_child
                    else:
                        succ.parent.right_child = succ.right_child
                    
            # one child 
            else:                                                
                if self.is_left_child():
                    if self.left_child:
                        self.parent.left_child = self.left_child
                    else:
                        self.parent.left_child = self.right_child
                elif self.is_right_child():
                    if self.left_child:
                        self.parent.right_child = self.left_child
                    else:
                        self.parent.right_child = self.right_child
                # root 
                else:
                    if self.left_child:
                        self.replace_node(value=self.left_child.value, left_child=self.left_child.left_child,
                                right_child=self.left_child.right_child, parent=None)                        
                    else:
                        self.replace_node(value=self.right_child.value, left_child=self.right_child.left_child,
                                right_child=self.right_child.right_child, parent=None)
        # 寻找要被删除的                        
        else:
            if self.value > data:
                if self.left_child:
                    self.left_child.delete(data)
                else:
                    return False 
            else:
                if self.right_child:
                    self.right_child.delte(data)
                else:
                    return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()
                
    def inorder(self):
        if self:            
            if self.left_child:
                self.left_child.preorder()
            print(str(self.value))
            if self.right_child:
                self.right_child.preorder()
                
    def postorder(self):
        if self:            
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()
            print(str(self.value))
    
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
            return True 
            
    def find(self, data):
        if self.root:
            self.root.find(data)
        else:
            return False
            
    def delete(self, data):
        #ipdb.set_trace()
        if self.root:
            self.root.delete(data)
        else:
            return False 
            
    def preorder(self):
        if self.root:
            self.root.preorder()
        else:
            return False 
            
    def inorder(self):
        if self.root:
            self.root.inorder()
        else:
            return False 
            
    def postorder(self):
        if self.root:
            self.root.postorder()
        else:
            return False                 
            
bst = Tree()            
bst.insert(10)
bst.insert(15)
bst.insert(1)
print(bst.inorder())
bst.delete(10)
print(bst.inorder())
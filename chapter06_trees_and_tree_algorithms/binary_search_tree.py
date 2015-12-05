class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size 
        
    def __len__(self):
        return self.size 
        
    def __iter__(self):
        return self.root.__iter__()
        
class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent 
        
    def has_left_child(self):
        return self.left_child
        
    def has_right_child(self):
        return self.right_child
        
    def is_left_child(self):
        # 存在 parent 需要注意
        return self.parent and self.parent.left_child == self 
        
    def is_right_child(self):
        return self.parent and self.parent.right_child == self
        
    def is_root(self):
        return not self.parent 
    
    def is_leaf(self):
        return not (self.left_child or self.right_child)
        
    def has_any_children(self):
        return self.right_child or self.left_child
        
    def has_both_children(self):
        return self.right_child and self.left_child
        
    def replace_node_data(self, key, value, lc, rc):
        self.key = key 
        self.payload = value 
        self.left_child = lc 
        self.right_child = rc 
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self 
            
       
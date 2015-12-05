class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size 
        
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            
    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val,
                    parent=current_node)
        
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val,
                    parent=current_node)
                    
    def __setitem__(self, k, v):
        self.put(k, v)
        
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None 
                
        else:
            return None
    
    def _get(self, key, current_node):
        if not current_node:
            return None 
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)
            
    def __getitem__(self, key):
        return self.get(key)
        
    # in operation 
    
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
            
       
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

    def find_successor(self):
        succ = None 
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self 
                    
        return succ 
        
    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current 
        
    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = self.left_child
            else:
                self.parent.right_child = self.left_child
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                # 有 children 就要告诉它它的爹是谁， 
                # 上面的 leaf 没有 children, 就只需要告诉它爷爷它的儿子变了
                self.left_child.parent = self.parent 
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else: 
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent
            
    
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
    def __contains__(self, key):
        if self._get(key, self.root):
            return True 
        else:
            return False 
            
    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None 
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree")
            
    def __delitem__(self, key):
        self.delete(key)
        
    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None 
        
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key 
            current_node.payload = succ.payload
        
        else: # this node has one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    # 有点绕 告诉孩子它的爷爷是谁，告诉它爷爷它孩子是谁
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.parent.right_child = current_node.left_child
                    current_node.left_child.parent = current_node.parent 
                else: # current_node 没 parent, 删除后儿子顶上 把 root 替换为儿子的值
                    current_node.replace_node_data(current_node.left_child.key,
                                    current_node.left_child.payload,
                                    current_node.left_child.left_child,
                                    current_node.left_child.right_child)
                                    
            # current_node 有右边的孩子
            else:                         
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                    current_node.right_child.payload,
                                    current_node.right_child.left_child,
                                    current_node.right_child.right_child)
                    
    
    def __len__(self):
        return self.size 
        
    def __iter__(self):
        return self.root.__iter__()
        

            
       
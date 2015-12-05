class BinaryTree:
    def __init__(self, root):
        self.key = root 
        self.left_child = None 
        self.right_child = None 
        
    def insert_left(self, new_node):
        t = BinaryTree(new_node)
        if self.left_child == None:
            self.left_child = t 
        else:
            t.left_child = self.left_child
            self.left_child = t 
    
    def insert_right(self, new_node):
        t = BinaryTree(new_node)
        if self.right_child == None:
            self.right_child = t 
        else:
            t.right_child = self.left_child
            self.right_child = t 
            
    def get_right_child(self):
        return self.right_child
        
    def get_left_child(self):
        return self.left_child
        
    def set_root_val(self, obj):
        self.key = obj 
        
    def get_root_val(self):
        return self.key  
        
def build_tree():
    r = BinaryTree('a')
    
    # left subtree 
    r.insert_left('b')
    r.get_left_child().insert_right('d')
    
    # right subtree 
    r.insert_right('c')
    r.get_right_child().insert_left('e')
    r.get_right_child().insert_right('f')
    
    print(r.get_root_val())
    
    print(r.get_left_child().get_root_val())
    print(r.get_left_child().get_right_child().get_root_val())
    
    print(r.get_right_child().get_root_val())
    print(r.get_right_child().get_left_child().get_root_val())    
    print(r.get_right_child().get_right_child().get_root_val())
    
build_tree()    
    
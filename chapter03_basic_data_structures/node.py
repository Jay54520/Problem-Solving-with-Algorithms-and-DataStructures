class Node():
    # 相比书中，添加一个 next 默认参数，可以在创建时有一个 next 索引
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data 
    
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
if __name__ == '__main__':
    temp = Node(99)
    print(temp.get_data())
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
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
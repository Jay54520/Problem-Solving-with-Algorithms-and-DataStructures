class Queue():
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
        
    def is_empty(self):
        # 不使用 len == 0，减少计算
        return self.items == []
        
    def size(self):
        return len(self.items)
        
        
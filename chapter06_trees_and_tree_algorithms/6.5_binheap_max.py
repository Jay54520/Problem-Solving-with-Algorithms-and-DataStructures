import ipdb

class BinHeap:
    def __init__(self):
        self.list = [0]
        self.index = 0
        
    def get_list(self):
        self.list.pop(0)
        return self.list
        
    def perc_up(self, index):
        while index // 2 > 0:
            if self.list[index] > self.list[index // 2]:
                self.list[index], self.list[index // 2] = self.list[index // 2], self.list[index]
                index //= 2
            else:
                return             
            
    def insert(self, val):
        self.list.append(val)
        self.index += 1
        self.perc_up(self.index)
        
            
    def del_min(self):
        stop = self.index // 2
        min = self.list[self.index]
        index = self.index - 1
        while index > stop:
            if self.list[index] < min:
                min = self.list[index]
            index -= 1 
        return_val = min        
        self.list.remove(min)
        self.index -= 1
        return return_val
        
    def build_heap(self, a_list):                
        self.index = len(a_list)
        self.list = [0] + a_list[:]
        index = self.index // 2 
        
        #ipdb.set_trace()
        while index > 0:            
            self.perc_down(index)
            index -= 1
            
    def perc_down(self, index):
        while 2 * index <= self.index:
            max_child = self.max_child(index)
            if self.list[index] < self.list[max_child]:
                self.list[index], self.list[max_child] = self.list[max_child], self.list[index]
            index = max_child
            
    def max_child(self, index):
        if 2 * index + 1 > self.index:
            return 2 * index 
        if self.list[2*index] > self.list[2*index + 1]:
            return 2 * index 
        else: 
            return 2 * index + 1
            
b = BinHeap()            
b.build_heap([3,2,5,9,6])
print(b.del_min())
b.insert(100)
print(b.get_list())

        
class BinHeap:
    def __init__(self):
        self.list = [0]
        self.index = 0
        
    def get_list(self):
        self.list.pop(0)
        return self.list
        
    def perc_up(self, index):
        while index > 0:
            if self.list[index] < self.list[index // 2]:
                self.list[index], self.list[index // 2] = self.list[index // 2], self.list[index]
                index //= 2
            else:
                return             
            
    def insert(self, val):
        self.list.append(val)
        self.index += 1
        self.perc_up(self.index)
        
    def perc_down(self, index):
        while (2 * index) <= self.index:
            min_child = self.min_child(index)
            if self.list[index] > self.list[min_child]:
                self.list[index], self.list[min_child] = self.list[min_child], self.list[index]
            index = min_child
            
    def min_child(self, index):
        if (2 * index + 1) > self.index:
            return 2 * index 
        if self.list[2 * index] < self.list[2 * index + 1]:
            return 2 * index
        else:
            return 2 * index + 1
            
    def del_min(self):
        return_val = self.list[1]
        self.list[1] = self.list[self.index]
        self.list.pop()
        self.index -= 1
        self.perc_down(1)
        return return_val
        
    def build_heap(self, a_list):                
        self.index = len(a_list)
        self.list = [0] + a_list[:]
        index = self.index // 2 
        while index > 0:            
            self.perc_down(index)
            index -= 1
            

if __name__ == '__main__'            :
    b = BinHeap()            
    b.build_heap([9,6,5,2,3])
    print(b.del_min())
    b.insert(100)
    print(b.get_list())

        
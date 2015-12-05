class BinHeap:
    def __init__(self):
        # [0] 不属于 current_size 因为他是凑数用的
        self.heap_list = [0]
        self.current_size = 0
        
    # 如果插入的数据小于它的 parent, 则两者互换位置
    # 直到位置为 1 ，即 root 的位置
    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            
            i = i // 2
            
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)
        
    def perc_down(self, i):               
        while (i * 2) <= self.current_size:
            # 返回 children 中最小的那个的位置
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        # 如果就只有左边，没有右边，直接返回左边
        if 2 * i + 1 > current_size:
            return 2 * i
        else:
            if self.heap_list[2 * i] < self.heap_list[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1
                
    def del_min(self):
        # 因为是递增顺序，所以 root 的值最小
        ret_val = self.heap_list[1]
        # 把最下面的移动到 root 的位置 
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val 
        
    def build_heap(self, a_list):
        # 因为 perc_down 中 2 * i <= current_size
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.perc_down(i)
            i -= 1 
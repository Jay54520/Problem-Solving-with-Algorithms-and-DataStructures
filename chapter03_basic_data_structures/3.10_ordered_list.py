from node import Node

class OrderedList:
    def __init__(self):
        self.head = None        
    
    def is_empty(self):
        return self.head == None
        
    def add(self, item):
        previous = None
        current = self.head
        stop = False 
        while current != None and not stop:            
            if current.get_data() > item:
                stop = True
            else:   
                previous = current
                current = current.get_next()
        
        temp = Node(item)
        if previous == None:                        
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
                        
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
            
        return count 
        
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                # 按递增顺序排列，如果当前值比所搜索的值大， 则停止
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        
        return found 
        
    def remove(self, item):
        current = self.head 
        previous = None
        found = False
        # 假定要删除的 Item 存在
        while not found:
            if current.get_data() == item:
                found = True
            else:
                # previous 指针指向 current, current 指向 current 的下一个
                previous = current
                current = current.get_next()
        
        # 如果 self.head 就是要找的
        if previous == None:
            self.head = self.head.get_next()
        else:
            previous.set_next(current.get_next())
    
    def print_list(self):
        current = self.head
        a_list = []
        while current != None:
            a_list.append(current.get_data())
            current = current.get_next()
        
        return a_list
        
if __name__ == "__main__":
    mylist = OrderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))

    mylist.add(100)
    print(mylist.search(100))
    print(mylist.size())

    mylist.remove(54)
    print(mylist.size())
    mylist.remove(93)
    print(mylist.size())
    mylist.remove(31)
    print(mylist.size())
    print(mylist.search(93))
    
    print(mylist.print_list())
        
            
            
        
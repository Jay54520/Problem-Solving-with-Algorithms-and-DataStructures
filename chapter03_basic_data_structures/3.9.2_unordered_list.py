from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None
        
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        if self.tail == None:
            self.tail = temp
            
        self.head = temp
        
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
        while current != None and not found:
            if current.get_data() == item:
                found = True
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
    
    def append(self, item):
        current = self.tail
        temp = Node(item)
        current.set_next(temp)
        current = current.get_next()
        
    def print_list(self):
        current = self.head
        a_list = []
        while current != None:
            a_list.append(current.get_data())
            current = current.get_next()
        
        return a_list
        
if __name__ == "__main__":
    mylist = UnorderedList()

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


    mylist.append(123)
    print(mylist.print_list())
        
            
            
        
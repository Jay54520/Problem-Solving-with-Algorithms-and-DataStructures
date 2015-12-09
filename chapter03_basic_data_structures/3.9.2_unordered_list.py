from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None 
        self.end = None 
    
    def is_empty(self):
        return self.head == None
        
    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.end = new_node
        
        new_node.set_next(self.head)
        self.head = new_node 
    
    def append(self, data):
        new_node = Node(data)
        self.end.set_next(new_node)
        self.end = new_node 
    
    def size(self):
        current = self.head 
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
            
        return count 
        
    def search(self, data):
        current = self.head 
        found = False 
        while current != None and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
                
        return found 
        
    def remove(self, data):
        previous = None
        current = self.head 
        found = False 

        while current != None and not found:
            if current.get_data() == data:
                found = True 
            else:
                previous = current 
                current = current.get_next()
            
        if not found:                                                                 
            raise ValueError('%s not exists.' % data)
        else:
            if current == self.head:
                self.head = self.head.get_next()
                return current.get_data()
            elif current == self.end:
                previous.set_next(None)
                self.end = previous 
                return current.get_data()
            else:
                previous.set_next(current.get_next())
                return current.get_data()
    
    # 如果没有 list [] 怎么打印出来？ 用 str ? 
    def __str__(self):
        current = self.head 
        a_list = []
        while current != None:
            a_list.append(str(current.get_data()))
            current = current.get_next()
            
        return ', '.join(a_list)
     
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
    mylist.append(123)
    print(mylist)                
from node import Node

class OrderedList:
    def __init__(self):
        self.head = None 
    
    def is_empty(self):
        return self.head == None
        
    def add(self, data):
        previous = None 
        current = self.head 
        new_node = Node(data)        
        
        # 如果需要递增：current.get_data() < data 时继续，大于等于 data 时停止
        # 如果需要递减：current.get_data() > data 时继续， 小于等于 data 时停止
        while current != None and current.get_data() < data:
            previous = current
            current = current.get_next()
            
        if current == None:
            if previous == None:
                self.head = new_node
            else:
                previous.set_next(new_node)                       
        else:
            if previous == None:
                new_node.set_next(self.head)
                self.head = new_node
            else:
                previous.set_next(new_node)
                new_node.set_next(current)
        
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
        while current != None and current.get_data() <= data and \
                not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
                
        return found 
        
    def remove(self, data):
        previous = None
        current = self.head 
        found = False         
        while current != None and current.get_data() <= data and \
                not found:
            if current.get_data() == data:
                found = True 
            else:
                previous = current 
                current = current.get_next()
            
        if not found:
            return False
            #raise ValueError('%s not exists.' % data)
        else:
            if current == self.head:
                self.head = self.head.get_next()
                return current.get_data()
            elif current.get_next() == None:
                previous.get_next(None)
            else:
                previous.set_next(current.get_next())
                return current.get_data()
                
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
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self, key, data):
        hash_value = self.hash_function(key)
        
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            # 被别的值占据了位置 寻找下一个位置
            else:
                next_slot = rehash(hash_value)
                while self.slots[next_slot] != None and \
                        self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)
                
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data
                    
    def hash_function(self, key):
        return key % self.size
        
    def rehash(self, old_hash_value):
        return (old_hash_value + 1) % self.size
        
    def get(self, key):
        start_slot = hash_function(key)
        
        data = None
        position = start_slot
        found = False
        stop = False
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = rehash(position)
                if position == start_slot:
                    stop = True
        return data
    
    def __getitem__(self, key):
        return self.get(key)
        
    def __setitem__(self, key, data):
        self.put(key, data)

if __name__ == '__main__':
    h=HashTable()
    h[54]="cat"
    h[26]="dog"
    print(h.slots) 
    print(h.data)
            
        
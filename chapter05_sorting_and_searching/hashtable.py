class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self, key, data):
        hash_value = self.hash_func(key)
        
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            # self.slots[hash_value] != key，储存了另一对 key, data
            else:
                next_hash_value = self.rehash(hash_value)
                while self.slots[next_hash_value] != None and \
                        self.slots[next_hash_value] != key:
                    next_hash_value = self.rehash(next_hash_value)
                
                if self.slots[next_hash_value] == None:
                    self.slots[next_hash_value] = key
                    self.data[next_hash_value] = data
                
                if self.slots[next_hash_value] == key:
                    self.data[next_hash_value] = data
    
    def hash_func(self, key):
        return key % self.size
        
    def rehash(self, old_hash):
        return (old_hash + 1) % self.size
        
    def get(self, key):
        start_slot = self.hash_func(key)
        
        data = None
        found = False
        stop = False
        position = start_slot
        
        while self.slots[position] != None and not found \
                and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True
        
        return data 
        
    def __getitem__(self, key):
        return self.get(key)
        
    def __setitem__(self, key, data):
        return self.put(key, data)
                    

if __name__ == '__main__':
    H=HashTable()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"    
    print(H.slots) 
    print(H.data)
            
        
def hash_string(a_string, table_size):
    sum = 0
    for pos in range(len(a_string)):
        sum = sum + ord(a_string[pos]) * (pos + 1)
        
    return sum % table_size
    
print(hash_string('cat', 11))
print(hash_string('dog', 11))
print(hash_string('rabbit', 11))
import timeit
import random
import ipdb

for i in range(10000, 1000000, 20000):
    # List index operator
    t = timeit.Timer('x[random.randrange(%d)]' % i, 'from __main__ import random, x')
    x = list(range(i))
    list_index_time = t.timeit(number=1000)
    #print('%d, %10.3f' % (i, list_index_time))
    # Verify the list index is O(1) because the time is about 
    # the same with the range(i) changes
    
    # Get item for dictionaries
    t = timeit.Timer('x.get(random.randrange(%d))' % i, 'from __main__ import random, x')
    x = {j:None for j in range(i)}    
    dict_get_time = t.timeit(number=1000)
    #print('%d, %10.3f' % (i, dict_get_time))
    
    # Set item for dictionaries
    t = timeit.Timer('x[random.randrange(%d)] = %d' % (i, i), 'from __main__ import random, x')
    x = {j:None for j in range(i)}
    dict_set_time = t.timeit(number=1000)
    #print('%d, %10.3f' % (i, dict_set_time))
    
    # Compares the performance of the del operator on lists and dictionaries
    #x = {j:None for j in range(i)}
    #为什么这里不能用引入？
    t = timeit.Timer('del {j:None for j in range(%d)}[random.randrange(%d)]' % (i, i), 'import random')        
    dict_del_time = t.timeit(number=1000)
    
    t = timeit.Timer('del list(range(%d))[random.randrange(%d)]' % (i, i), 'from __main__ import random, x')
    #x = list(range(i))
    list_del_time = t.timeit(number=1000)
    print('%d, %10.3f, %10.3f' % (i, list_del_time, dict_del_time))
    
    
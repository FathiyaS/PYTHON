hash_table = [[] for _ in range (5)]

def hashing_func (key):
    return key % len (hash_table)

print (hashing_func (25))
print (hashing_func (76))
print (hashing_func (63))
print (hashing_func (98))
print (hashing_func (58))
print (hashing_func (19))


def insert (hash_table, key, value):
    hash_key = hashing_func (key)
    hash_table [hash_key].append(value)
    
insert (hash_table, 25, 'Malaysia')
insert (hash_table, 76, 'Indonesia')
insert (hash_table, 63, 'Singapura')
insert (hash_table, 98, 'Vietnam')
insert (hash_table, 58, 'Thailand')
insert (hash_table, 19, 'Filipina')
print (hash_table)

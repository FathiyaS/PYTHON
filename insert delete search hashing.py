hash_table = [[] for _ in range (10)]

def insert (hash_table, key, value):
    hash_key = hash (key) % len (hash_table)
    key_exists = False 
    bucket = hash_table [hash_key] 
    for i, kv in enumerate (bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket [i] = ((key, value))
    else:
        bucket.append((key, value))

def search (hash_table, key) :
    hash_key = hash (key) % len (hash_table)
    bucket = hash_table [hash_key]
    for i, kv in enumerate (bucket):
        k, v = kv
        if key == k:
            return v

def delete (hash_table, key) :
    hash_key = hash (key) % len (hash_table)
    key_exists = False 
    bucket = hash_table [hash_key]
    for i, kv in enumerate (bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break

    if key_exists:
        del bucket [i]
        print ('Key {} deleted'.format (key))
    else:
        print ('Key {} not found'.format (key))

insert (hash_table, 10, 'Solo')
insert (hash_table, 15, 'Sukoharjo')
insert (hash_table, 20, 'Wonogiri')
insert (hash_table, 25, 'Sragen')
insert (hash_table, 30, 'Karanganyar')
insert (hash_table, 35, 'Boyolali')
print (hash_table)
print(search(hash_table,10))
delete(hash_table,15)
print (hash_table)


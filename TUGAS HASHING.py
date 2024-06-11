hash_table = [{} for _ in range (10)]

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
        

insert ( hash_table,{35:{'Kode' : 'A','Judul':'Pemrograman dasar','Pengarang' : 'Abdul Khadir','Penerbit':'Andi'}})
print(search(hash_table,35))

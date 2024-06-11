hash_table = ["Hello"]*10
print (hash_table)

def hash_func(key):
    return key% len (hash_table)

def insert(hash_table, key, value):
    hash_key = hash_func(key)
    hash_table[hash_key] = value

insert(hash_table, 10,"Solo")
insert(hash_table, 20,"Wonogiri")
insert(hash_table, 25,"Sragen")
print(hash_table)

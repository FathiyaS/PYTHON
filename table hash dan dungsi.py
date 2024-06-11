hash_table = ["Hello"]*10
print (hash_table)

def hash_func(key):
    return key% len (hash_table)

print(hash_func(10))
print(hash_func(20))
print(hash_func(25))


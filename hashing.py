kota = [
    [10,"Solo"],
    [15,"Sukoharjo"],
    [20,"Wonogiri"],
    [25,"Sragen"],
    [30,"Karanganyar"],
    [35,"Boyolali"]
]

def insert(item_list, key, value):
    item_list.append((key, value))
    
def search(item_list,  key):
    for item in item_list:
        if item[0] == key:
            return item[1]


for key, value in kota:
    print(key,"->",value)

insert(kota,40,"Salatiga")
print(kota)
print(search(kota,15))

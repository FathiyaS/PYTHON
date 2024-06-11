def q_sort (a, low, high):
    if low<high:
        pivotpos=partition (a, low, high)
        q_sort (a, low, pivotpos-1)
        q_sort (a, pivotpos+1, high)

def partition (a, low, high):
    pivotvalue=a[low]
    up=low+1
    down=high
    done=False
    while not done:
        while up<=down and a [up]<=pivotvalue:
            up+=1
        while down>=up and a [down] >=pivotvalue:
            down-=1
            if down<up:
                done=True
            else:
                temp=a [up]
                a [up]=a [down]
                a [down]=temp
        temp=a[low]
        a [low]=a[down]
        a [down]=temp
        return down
a =[
["Billy",2022010003, "Semarang"],
["Roby",2022010005, "Salatiga"],
["Nadine",2022010002,"Yogyakarta"],
["Joshua",2022010004, "Yogyakarta"],
["Ruby",2022010001, "Solo"]
]
high=len(a)
q_sort (a,0, high-1)
print ("DATA MAHASISWA BERDASARKAN ASAL")
for Nama, NIM, Asal in a:
    print (NIM, "|", Nama, "|", Asal)

def m_sort(a):
    for i in range(len(a)):
        if i>1:
            mid=len(a)//2
            l_half=a[:mid]
            r_half=a[mid:]
            m_sort(l_half)
            m_sort(r_half)
            i=j=k=0
            while i<len(l_half)and j<len(r_half):
                if l_half[i]<r_half[j]:
                    a[k]=l_half[i]
                    i+=1
                else:
                    a[k]=r_half[j]
                    j+=1
                k+=1
            while i<len(l_half):
                a[k]=l_half[i]
                i+=1
                k+=1
            while j<len(r_half):
                a[k]=r_half[j]
                j+=1
                k+=1

a =[
["Billy",2022010003, "Semarang"],
["Roby",2022010005, "Salatiga"],
["Nadine",2022010002,"Yogyakarta"],
["Joshua",2022010004, "Yogyakarta"],
["Ruby",2022010001, "Solo"]
]
m_sort(a)
print ("DATA MAHASISWA BERDASARKAN ASAL")
for Nama, NIM, Asal in a:
    print (Asal, "|", Nama, "|", NIM)

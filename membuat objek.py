class bunga :
    def __init__(self,nama,warna):
        self.nama = nama
        self.warna = warna

    def deskripsi (self):
        print ("Nama bunga:",self.nama)

    def wrn(self):
        print("Warna Bunga :", self.warna)
        

bga = bunga("Dandelions","putih")
print("********************************")
bga.deskripsi()
bga.wrn()
print("********************************")
bga1 = bunga("Mawar","merah")
bga1.deskripsi()
bga1.wrn()
print("********************************")
bga2 = bunga("Melati","putih")
bga2.deskripsi()
bga2.wrn()
print("********************************")



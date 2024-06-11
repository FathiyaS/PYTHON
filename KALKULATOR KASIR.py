harga = []
pesanan = []
total_pembayaran =0
while True :
    print ("===============================Daftar harga===================================")
    print ("|----------------------------------------------------------------------------|")
    print ("|  Kode |            Ukuran                 |               Harga(Rp)        |")
    print ("|----------------------------------------------------------------------------|")
    print ("|   1   |Cone (maksimal 2 rasa)             |               30.000           |")
    print ("|   2   |Cup Small (maksimal 2 rasa)        |               25.000           |")
    print ("|   3   |Cup medium (maksimal 3 rasa)       |               45.000           |")
    print ("|   4   |Cup big (maksimal 2  rasa)         |               70.000           |")
    print ("|   5   |Cup extra big (maksimal 2 rasa)    |               120.000          |")

    kode = int(input("Masukkan kode pesanan : "))
    if kode == 1:
        pesanan.append("Cone (maksimal 2 rasa)")
        harga.append(30000)
        total_pembayaran +=30000
    else:
        ("Kode tidak ada")

    pesanan_lain = input("Ada pesanan dengan ukuran yang berbeda ?\nTekan (YES/NO) : ")
    if pesanan_lain == "NO" :
        print ("")
        break

print ("Ukuran gelato : ", pesanan)
print ("Pesanan : Rp.", harga)
print ("Total pembayaran : Rp.", total_pembayaran)

bayar = int(input("Bayar Rp."))
if bayar > total_pembayaran:
    print("Sisa uang kembali :Rp.",bayar - total_pembayaran)
            
                
            

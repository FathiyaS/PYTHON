try:
    class queue:
        def __init__(self,n=30):
            self.size = n
            self.current_size = 0
            self.name = []
            self.size = []
            self.flavor = []
            self.pesanan = []
            self.harga = []
            self.total_pembayaran = 0
            
        def isFull(self):
            if self.current_size == self.size:
                return True
            else :
                return False
            
        def isEmpty(self):
            if self.current_size == 0:
                return True
            else :
                return False
            
        def enqueue(self,nama,ukuran,rasa):
            if self.isFull():
                print("Mohon maaf antrian sudah penuh")
            else :
                self.name.append(nama)
                self.size.append(ukuran)
                self.flavor.append(rasa)
                self.current_size = len(self.name)
                print ("----detail pesanan---")
                print ("Nama : ",nama)
                print ("Ukuran : ",ukuran)
                print ("Varian Rasa : ",rasa)
                print("Pesanan atas nama ",nama, " akan segera kami buat silahkan menunggu, Terima kasih ^o^")
            print("Tekan [enter] untuk melanjutkan")
            input()
            self.menu()
            

        def dequeue(self):
            if self.isEmpty():
                print("Maaf antrian masih kosong")
                return None
            else:
                datakeluar = self.name.pop(0)
                ukuran = self.size.pop(0)
                rasa = self.flavor.pop(0)
                self.current_size = len(self.name)
                print("-------------------------")
                print("Pesanan atas nama:",datakeluar,"sudah siap, silahkan ambil pesanan anda")
                print("----- Detail Pesanan-----")
                print("Nama : ", datakeluar)
                print("Ukuran : ", ukuran)
                print("Rasa : ", rasa)
                print("-------------------------")
            print("Lanjutkan dan pilih menu pembayaran")
            input()
            self.menu()
            
        def view(self):
            if self.isEmpty():
                print("Mohon maaf antrian masih kosong")
            else:
                print("=======DAFTAR ANTRIAN=====")
                X = 1
                for i in self.name:
                    print(" "+str(X)+". ",i)
                    X +=1
                print("Total Antrian :", len(self.name))
            print("Tekan [enter] untuk melanjutkan")
            input()
            self.menu()

        def bill(self,pesanan,harga,total_pembayaran):
            if self.isFull():
                print("Mohon maaf antrian sudah penuh")                
            else :
                self.pesanan.append(pesanan)
                self.harga.append(harga)
                self.total_pembayaran +=0
                self.current_size = len(self.name)
                
            print("Tekan [enter] untuk melanjutkan")
            input()
            self.menu()
                
        def Exit(self):
            print("Anda telah keluar dari program")
            import sys
            sys.exit()

        def menu(self):
            import os
            os.system("CLS")
            print ("==============================================================================================")
            print ("|                           SELAMAT DATANG DI TOKO GELATO KAMI                               |")
            print ("==============================================================================================")
            print ("|------------------------------------ MENU KASIR --------------------------------------------|")
            print ("|1. Memasukkan Pesanan                                                                       |")
            print ("|2. Pesanan Siap                                                                             |")
            print ("|3. Daftar Antrian Pelanggan                                                                 |")
            print ("|4. Pembayaran                                                                               |")
            print ("|5. Exit                                                                                     |")
            print ("==============================================================================================")

            pil = int(input("Masukan no menu yang ingin dipilih:"))

            if pil ==1:
                print ("")
                print ("-----------------------------------------------------------------------------------------------")
                print ("   Terimakasih telah melakukan pemesanan silahkan memilih ukuran dan rasa yang anda inginkan   ")
                print ("-----------------------------------------------------------------------------------------------")
                print ("========================================Daftar harga===========================================")
                print ("|   Ukuran                                    |                              Harga(Rp)        |")
                print ("|   Cone (maksimal 2 rasa)                    |                              30.000           |")
                print ("|   Cup Small (maksimal 2 rasa)               |                              25.000           |")
                print ("|   Cup medium (maksimal 3 rasa)              |                              45.000           |")
                print ("|   Cup big (maksimal 2  rasa)                |                              70.000           |")
                print ("|   Cup extra big (maksimal 2 rasa)           |                              120.000          |")
                print ("-----------------------------------------------------------------------------------------------")
                print ("==================================Varian Rasa Gelato===========================================")
                print ("==========================Ada 30 varian rasa yang tersedia=====================================")
                print ("|  - banana                        -banana caramel                        -banana choco       |")
                print ("|  - black coffee                  -cappuccino                            -caramel mix fruit  |")
                print ("|  - cashew nut                    -cheese                                -chocolate          |")
                print ("|  - choco Davos                   -choco mint                            -chocomilk          |")
                print ("|  - cinnamon                      -coconut                               -coconut choco      |")
                print ("|  - coffee                        -coffee caramel                        -Davos              |")
                print ("|  - Kit-Kat                       -Krokante                              -lemon grass        |")
                print ("|  - matcha tea                    -mint                                  -mint choco         |")
                print ("|  - Nutella                       -Oreo                                  -pistachio          |")
                print ("-----------------------------------------------------------------------------------------------")
                print ("-----------------------------------------------------------------------------------------------")
                print ("-----------------------------------------------------------------------------------------------")
                print ("*******************************MASUKKAN PESANAN PELANGGAN**************************************")
                print ("Nb = Jika pesanan lebih dari satu maka pesanan dikelompokkan manual dengan tanda kurung ukuran searah dengan pilihan rasa : ")
                nama = input("Nama pelanggan : ")
                ukuran = input ("Ukuran tempat : ")
                rasa = input("Varian Rasa : ")
                self.enqueue(nama,ukuran,rasa)
                
            elif pil == 2:
                self.dequeue()
            elif pil == 3:
                self.view()
            elif pil == 4:
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
                        self.total_pembayaran +=30000
                    elif kode == 2:
                        self.pesanan.append("Cup Small (maksimal 2 rasa)")
                        self.harga.append(25000)
                        self.total_pembayaran +=25000
                    elif kode == 3:
                        self.pesanan.append("Cup medium (maksimal 3 rasa))")
                        self.harga.append(45000)
                        self.total_pembayaran +=45000
                    elif kode == 4:
                        self.pesanan.append("Cup big (maksimal 2  rasa)")
                        self.harga.append(70000)
                        self.total_pembayaran +=70000
                    elif kode == 5:
                        self.pesanan.append("Cup extra big (maksimal 2 rasa)")
                        self.harga.append(120000)
                        self.total_pembayaran +=120000
                    else:
                        ("Kode tidak ada")

                    pesanan_lain = input("Ada pesanan dengan ukuran yang berbeda ?\nTekan (YES/NO) : ")
                    if pesanan_lain == "NO" :
                        print ("")
                        break
                print("Ukuran : ", self.pesanan)
                print("harga : ", self.harga)    
                print ("Total pembayaran : Rp.", self.total_pembayaran)
                print ("TerimakasiH, selamat menikmati")
                self.bill(self.pesanan,self.harga,self.total_pembayaran)
                
            elif pil == 5:
                self.Exit
            else:
                print("Mohon maaf pilihan anda tidak ada silahkan ulangi kembali")
                print("Tekan [enter] untuk kembali ke menu")
                input()
                self.menu()
    q = queue()
    q.menu()
except ValueError:
    print("Program hanya bertipe integer")
    print("Silahkan mulai kembali program!")
          

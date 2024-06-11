try:
    class queue:
        def __init__(self,n=30):
            self.size = n
            self.current_size = 0
            self.name = []
            self.uk = []
            self.favour = []
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
        def enqueue(self,name,uk, favour):
            if self.isFull():
                print("Mohon maaf antrian sudah penuh")
            else :
                self.name.append(name)
                self.uk.append(uk)
                self.favo.append(favourr)
                self.current_size = len(self.name)
                print ("----detail pesanan---")
                print ("Nama : ",name)
                print ("Ukuran : ",uk)
                print ("Varian Rasa : ",favour)
                print("Pesanan atas nama ",name, " akan segera kami buat silahkan menunggu, Terima kasih ^o^")
            self.menu()
            

        def dequeue(self):
            if self.isEmpty():
                print("Maaf antrian masih kosong")
                return None
            else:
                datakeluar = self.name.pop(0)
                self.current_size = len(self.name)
                print("-------------------------")
                print("Pesanan atas nama:",datakeluar,"sudah siap, silahkan ambil pesanan anda")
                print("-------------------------")
            print("Tekan [enter] untuk melanjutkan")
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
            print ("|---------- Silahkan pilih menu [PESAN] dibawah ini untuk melakukan pemesanan ---------------|")
            print ("|1. Pesan gelato                                                                             |")
            print ("|2. Ambil Pesanan                                                                            |")
            print ("|3. Lihat Daftar Antrian                                                                     |")
            print ("|4. Exit                                                                                     |")
            print ("==============================================================================================")

            pil = int(input("Masukan no menu yang ingin dipilih:"))

            if pil ==1:
                print ("")
                print ("-----------------------------------------------------------------------------------------------")
                print ("Terimakasih telah melakukan pemesanan berikut daftar harga dan varian rasa yang bisa anda pilih")
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
                name = input("nama pelanggan : ")
                uk = input ("ukuran tempat : ")
                favour = input("Masukkan varian  : ")
                self.enqueue(name,uk,favour)
                
            elif pil == 2:
                self.dequeue()
            elif pil == 3:
                self.view()
            elif pil == 4:
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
          

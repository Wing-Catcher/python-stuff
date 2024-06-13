# Project membuat kalkulator based on rectangle
print("======================================================")
print("Selamat datang di program Kalkulator Persegi Panjang")
print("*Hanya mendukung input bilangan bulat dan bukan desimal")
print("Dibuat oleh: Raffy IX-B/19")
print("======================================================")

def kalkulator ():
    # bagian memilih mode kalkulator
    print("Silahkan pilih mode kalkulator: ")
    print("(a) Mencari luas")
    print("(b) Mencari Keliling")
    print("(c) Mencari komponen dari persegi panjang")
    print("(d) Tentang")
    print("v.2.4 (final)")
    print()
    pilihan = input("Pilihan: ")

    # eksekusi pilihan cari luas
    if pilihan == "a":
        print()
        # menerima input dari user
        panjang = input("Masukkan panjang persegi panjang: ")
        lebar = input("Masukkan lebar persegi panjang: ")
        # kondisi terkait isdigit
        if panjang.isdigit() and lebar.isdigit():
            panjang, lebar = int(panjang), int(lebar)
            luas = panjang * lebar
            if panjang > lebar:
                input("Klik enter untuk menampilkan hasil")
                print()
                print("Luas persegi panjang adalah: " + str(luas))
                mengulang()
            elif panjang == lebar:
                input("Klik untuk menampilkan hasil")
                print()
                print("Luas persegi adalah: " + str(luas))
                mengulang()
            else:
                print()
                input("Input panjang lebih kecil daripada lebar. Menghentikan phyton. Klik enter untuk keluar.")
                mengulang()
        #kondisi bukan isdigit, keluar python dengan enter
        else:
            print()
            print("Input selain angka terdeteksi. Menghentikan python")
            input("Klik enter untuk keluar")
            mengulang()
    # eksekusi mencari keliling
    elif pilihan == "b":
        print()
        # menerima input dari user
        panjang = input("Masukkan panjang persegi panjang: ")
        lebar = input("Masukkan lebar persegi panjang: ")
        # kondisi terkait isdigit
        if panjang.isdigit() and lebar.isdigit():
            panjang, lebar = int(panjang), int(lebar)
            keliling = 2*(panjang + lebar)
            if panjang > lebar:
                input("Klik enter untuk menampilkan hasil")
                print()
                print("Keliling persegi panjang adalah: " + str(keliling))
                mengulang()
            elif panjang == lebar:
                input("Klik untuk menampilkan hasil")
                print()
                print("Keliling persegi adalah: " + str(keliling))
                mengulang()
            else:
                print()
                input("Input panjang lebih kecil daripada lebar. Menghentikan phyton. Klik enter untuk keluar.")
                mengulang()
        #kondisi bukan isdigit, keluar python dengan enter
        else:
            print()
            print("Input selain angka terdeteksi. Menghentikan python")
            input("Klik enter untuk keluar")
            mengulang()
    # eksekusi pilihan c
    elif pilihan == "c":
        # listing sub mode
        print()
        print("Anda memilih c, silahkan pilih mode kalkulator: ")
        print()
        print("SEGMEN MENCARI PANJANG: ")
        print("(a1) Diketahui lebar dan keliling")
        print("(a2) Diketahui lebar dan luas")
        print()
        print("SEGMEN MENCARI LEBAR: ")
        print("(b1) Diketahui Panjang dan keliling")
        print("(b2) Diketahui Panjang dan luas")
        print()
        pilihan = input("Pilihan: ")
        # jika user input (a1)
        if pilihan == "a1":
            print()
            lebar = input("Lebar yang diketahui: ")
            keliling = input("Keliling yang diketahui: ")
            # input harus digit
            if lebar.isdigit() and keliling.isdigit():
                # konversi nilai ke integer
                lebar, keliling = int(lebar), int(keliling)
                panjang = (keliling - (2 * lebar)) / 2
                # ga mungkin lah kalo hasilnya minus, kita pisahin saja 
                if panjang > 0:
                    print()
                    input("Klik enter untuk menampilkan hasil")
                    print("Panjang dari persegi panjang adalah: " + str(panjang))
                    input("Klik enter untuk keluar")
                    mengulang()
                else:
                    print()
                    print("Hasil Invalid (negatif) --> " + str(panjang) + " cek kembali input anda.")
                    input("Klik enter untuk keluar.")
                    mengulang()
            else:
                print()
                print("Input selain angka terdeteksi. Menghentikan python")
                input("Klik enter untuk keluar.")
                mengulang()
        # ngeladenin input a2
        elif pilihan == "a2":
            print()
            lebar = input("Lebar yang diketahui: ")
            luas = input("Luas yang diketahui: ")
            # keduanya harus digit
            if lebar.isdigit() and luas.isdigit():
                lebar, luas = int(lebar), int (luas)
                panjang = luas / lebar
                print()
                # tidak mungkin = 0, jadi..
                if panjang > 0:
                    input("Klik enter untuk menampilkan hasil")
                    print("Panjang dari persegi panjang adalah: " + str(panjang))
                    input("Klik enter untuk keluar.")
                    mengulang()
                else:
                    print("Hasil Invalid (negatif) --> " + str(panjang) + " cek kembali input anda.")
                    print("Klik enter untuk keluar.")
                    mengulang() #akhir segmen mencari panjang fyuhh..
            else:
                print()
                print("Input selain angka terdeteksi. Menghentikan python")
                input("Klik enter untuk keluar.")
                mengulang()
                
        # ngeladenin input b1
        elif pilihan == "b1":
            print()
            panjang = input("Panjang yang diketahui: ")
            keliling = input("Keliling yang diketahui: ")
            # keduanya harus bcerupa digit jadi..
            if panjang.isdigit() and keliling.isdigit():
                panjang, keliling = int(panjang), int(keliling)
                lebar = (keliling - (2 * panjang)) / 2
                print()
                # sama kek tadi gamungkin 0
                if lebar > 0:
                    input("Klik untuk menampilkan hasil")
                    print("Lebar dari persegi panjang adalah: " + str(lebar))
                    input("Klik enter untuk keluar.")
                    mengulang()
                else:
                    print("Hasil Invalid (negatif) --> " + str(lebar) + " cek kembali input anda.")
                    input("Klik enter untuk keluar.")
                    mengulang()
            else:
                print()
                print("Input selain angka terdeteksi. Menghentikan python.")
                input("Klik enter untuk keluar")
                mengulang()
        # ngeladenin b2
        elif pilihan == "b2":
            print()
            panjang = input("Panjang yang diketahui: ")
            luas = input("Luas yang diketahui: ")
            if panjang.isdigit() and luas.isdigit():
                panjang, luas = int(panjang), int(luas)
                lebar = luas / panjang
                print()
                if lebar > 0:
                    input("Klik untuk menampilkan hasil")
                    print("Lebar dari persegi panjang adalah: " + str(lebar))
                    input("Klik enter untuk keluar.")
                    mengulang()
                else:
                    print("Hasil Invalid (negatif) --> " + str(lebar) + " cek kembali input anda.")
                    input("Klik enter untuk keluar.")
                    mengulang()
            else:
                print()
                print("Input selain angka terdeteksi. Menghentikan python.")
                input("Klik enter untuk keluar.")
                mengulang()
        # menabok yang ngeyel bukan a1 a2 b1 b2..
        else:
            print("Input invalid, bukan a1, a2, b1, b2. Menghentikan python")
            input("Klik enter untuk keluar")
            mengulang()
    # menabok yang ngeyel lagi bukan a b atau c..
    elif pilihan == "d":
        print()
        print("Kalkulator persegi panjang sederhana oleh Raffy IX-B")
        print("Menggunakan bahasa pemrogaman python dan dibuat di Visual Code")
        print("Lisensi gratis, modifikasi bebas. Dilarang monetisasi")
        print("Versi 2.4 (final)")
        print("'sudah berusaha belajar'")
        print()
        mengulang()
    else:
        print("Input invalid, bukan a, b, c. Menghentikan python.")
        input("Klik enter untuk keluar")
        mengulang()
#def untuk mengulang
def mengulang():
    ulang = input("Program selesai, apakah anda ingin mengulang? (ya/tidak): ")
    print("======================================================")
    if ulang == "ya":
        kalkulator()
    elif ulang == "tidak":
        input("Oke, klik enter untuk keluar")
    else:
        input("Input invalid. Klik enter untuk keluar.")
# eksekusi def utama untuk awalan
kalkulator()
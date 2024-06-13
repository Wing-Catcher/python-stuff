"""
Project: long

Pesan untuk diri sendiri:
Keep up bro, pantang menyerah. Kita bisa bikin ini:
Kalkulator Bangun Datar Umum
:)
Notes (Taruh disini)
- selalu konversi ke float, support desimal, dan returning point
"""
import math
import time
import os
# definisi utama, memuat tampilan home dan fungsi semua bangun
def main():
    # Bangun 2D: Persegi
    def persegi():
        #Bagian implementasi rumus dengan float casting
        def luas_persegi(sisi):
            sisi = float(sisi)
            luas = sisi * sisi
            return luas
        def keliling_persegi(sisi):
            sisi = float(sisi)
            keliling = sisi * 4
            return keliling
        def sisi_dari_luas (luas):
            luas = float(luas)
            sisi = math.sqrt(luas)
            return sisi
        def sisi_dari_keliling(keliling):
            keliling = float(keliling)
            sisi = keliling / 4
            return sisi
        def diagonal_persegi(sisi):
            sisi = float(sisi)
            diagonal = sisi * math.sqrt(2)
            return diagonal
        #Bagian tampilan terminal
        print(r"   __    ____    ____                          _ ")
        print(r"  / /   / /\ \  |  _ \ ___ _ __ ___  ___  __ _(_)")
        print(r" / /   / /  \ \ | |_) / _ \ '__/ __|/ _ \/ _` | |")
        print(r" \ \  / /   / / |  __/  __/ |  \__ \  __/ (_| | |")
        print(r"  \_\/_/   /_/  |_|   \___|_|  |___/\___|\__, |_|")
        print(r"                                         |___/   ")
        print()
        print("=== Bangun Terpilih: Persegi ===")
        print()
        print("Silahkan pilih mode untuk bangun persegi:")
        print("A = Mencari luas persegi")
        print("B = Mencari keliling persegi")
        print("C = Advanced")
        print()
        pilihan = None
        while not pilihan:
            pilihan = input("Pilihan: ").lower()
        print()
        if pilihan == "a":
            sisi = None
            while not sisi:
                sisi = input("Sisi persegi: ")
            print()
            if "-" in sisi:
                print("Error: Tidak bisa melakukan input negatif.")
            elif "." in sisi or sisi.isdigit():
                try:
                    hasil = luas_persegi(sisi)
                    print("Luas persegi adalah: " + str(hasil))
                except ValueError:
                    print("Error: Kesalahan input.")
            else:
                print("Error: Kesalahan input.")
        elif pilihan == "b":
            sisi = None
            while not sisi:
                sisi = input("Sisi persegi: ")
            if "-" in sisi:
                print("Error: Tidak bisa melakukan input negatif.")
            elif "." in sisi or sisi.isdigit():
                try:
                    hasil = keliling_persegi(sisi)
                    print("Keliling persegi adalah: " + str(hasil))
                except ValueError:
                    print("Error: Kesalahan input.")
            else:
                print("Error: Kesalahan input.")
        elif pilihan == "c":
            print("=== Advanced: Persegi ===")
            print()
            print("A = Mencari sisi dari diketahui luas")
            print("B = Mencari sisi dari diketahui keliling")
            print("C = Mencari diagonal persegi")
            print()
            pilihan = None
            while not pilihan:
                pilihan = input("Pilihan: ").lower()
            print()
            if pilihan == "a":
                luas = None
                while not luas:
                    luas = input("Luas persegi: ")
                if "-" in luas:
                    print("Error: Tidak bisa melakukan input negatif.")
                elif "." in luas or luas.isdigit():
                    try:
                        hasil = sisi_dari_luas(luas)
                        print()
                        print("Sisi persegi adalah: " + str(hasil))
                    except ValueError:
                        print("Error. Kesalahan input.")
            elif pilihan == "b":
                keliling = None
                while not keliling:
                    keliling = input("Keliling persegi: ")
                if "-" in keliling:
                    print("Error: Tidak bisa melakukan input negatif.")
                elif "." in keliling or keliling.isdigit():
                    try:
                        hasil = sisi_dari_keliling(keliling)
                        print()
                        print("Sisi persegi adalah: " + str(hasil))
                    except ValueError:
                        print("Error. Kesalahan input.")
            elif pilihan == "c":
                sisi = None
                while not sisi:
                    sisi = input("Sisi persegi: ")
                if "-" in sisi:
                    print("Error. Tidak bisa melakukan input negatif.")
                elif "." in sisi or sisi.isdigit():
                    try:
                        hasil = diagonal_persegi(sisi)
                        print()
                        print("Diagonal persegi adalah: " + str(hasil))
                    except ValueError:
                        print("Error. Kesalahan input.")
                else:
                    print("Error. Kesalahan input.")
            else:
                print("Error. Kesalahan input")
        else:
            print("Error. Kesalahan input.")
        time.sleep(3)
        print()
        print("=== Eksekusi sukses ===")
        print("=== DEBUG: exit code 0 ===")
        repeat()
    # Bangun 2D: Persegi Panjang
    def persegi_panjang():
        # Menggunakan alias rectangle
        # panjang = p, lebar = l
        def luas_rectangle(p, l):
            p, l = float(p), float(l)
            luas = p * l
            return luas
        def keliling_rectangle(p, l):
            p, l = float(p), float(l)
            keliling = 2 * (p + l)
            return keliling
        # Advanced: Mencari panjang
        def panjang_lebarluas(l, luas):
            l, luas = float(l), float(luas)
            panjang = luas / l
            return panjang
        def panjang_lebarkeliling(l, keliling):
            l, keliling = float(l), float(keliling)
            panjang = (keliling - l)/2
            return panjang
        # Advanced: Mencari lebar
        def lebar_panjangluas(p, luas):
            p, luas = float(p), float(luas)
            lebar = luas / p
            return lebar
        def lebar_panjangkeliling(p, keliling):
            p, keliling = float(p), float(keliling)
            lebar = (keliling - p)/2
            return lebar
        # Advanced: Diagonal
        def diagonal_rectangle(p, l):
            p, l = float(p), float(l)
            diagonal = math.sqrt((math.pow(p,2) + math.pow(l,2)))
            return diagonal
        # Bagian tampilan terminal
        print(r"   __    ____    ____                          _   ____              _                   ")
        print(r"  / /   / /\ \  |  _ \ ___ _ __ ___  ___  __ _(_) |  _ \ __ _ _ __  (_) __ _ _ __   __ _ ")
        print(r" / /   / /  \ \ | |_) / _ \ '__/ __|/ _ \/ _` | | | |_) / _` | '_ \ | |/ _` | '_ \ / _` |")
        print(r" \ \  / /   / / |  __/  __/ |  \__ \  __/ (_| | | |  __/ (_| | | | || | (_| | | | | (_| |")
        print(r"  \_\/_/   /_/  |_|   \___|_|  |___/\___|\__, |_| |_|   \__,_|_| |_|/ |\__,_|_| |_|\__, |")
        print(r"                                         |___/                    |__/             |___/ ")
        print()
        print("=== Bangun terpilih: Persegi Panjang ===")
        print()
        print("Silahkan pilih mode untuk bangun Persegi panjang:")
        print("A = Mencari luas persegi panjang")
        print("B = Mencari keliling persegi panjang")
        print("C = Advanced")
        print()
        pilihan = None
        panjang = None
        lebar = None
        luas = None
        keliling = None
        while not pilihan:
            pilihan = input("Pilihan: ").lower()
        print()
        if pilihan =="a":
            while not panjang:
                panjang = input("Sisi panjang: ")
            while not lebar:
                lebar = input("Sisi lebar: ")
            print()
            if ("-" in panjang) or ("-" in lebar):
                print("Error: Tidak bisa melakukan input negatif.")
            elif ("." in panjang or panjang.isdigit()) and ("." in lebar or lebar.isdigit()):
                try:
                    hasil = luas_rectangle(panjang, lebar)
                    print("Luas persegi panjang adalah: " + str(hasil))
                except ValueError:
                    print("Error: Kesalahan input.")
            else:
                print("Error: Kesalahan input.")
        elif pilihan == "b":
            while not panjang:
                panjang = input("Sisi panjang: ")
            while not lebar:
                lebar = input("Sisi lebar: ")
            print()
            if ("-" in panjang) or ("-" in lebar):
                print("Error: Tidak bisa melakukan input negatif.")
            elif ("." in panjang or panjang.isdigit()) and ("." in lebar or lebar.isdigit()):
                try:
                    hasil = keliling_rectangle(panjang, lebar)
                    print("Keliling persegi panjang adalah: " + str(hasil))
                except ValueError:
                    print("Error: Kesalahan input")
            else:
                print("Error: Kesalahan input.")
        elif pilihan == "c":
            print("=== Advanced: Persegi Panjang ===")
            print()
            print("</> SISI PANJANG")
            print("A1 = Mencari panjang dari lebar dan luas")
            print("A2 = Mencari panjang dari lebar dan keliling")
            print()
            print("</> SISI LEBAR")
            print("B1 = Mencari lebar dari panjang dan luas")
            print("B2 = Mencari lebar dari panjang dan keliling")
            print()
            print("</> LAIN-LAIN")
            print("C1 = Mencari diagonal persegi panjang")
            print()
            pilihan = None
            while not pilihan:
                pilihan = input("Pilihan: ").lower()
            print()
            if pilihan == "a1":
                while not lebar:
                    lebar = input("Sisi lebar: ")
                while not luas:
                    luas = input("Luas persegi panjang: ")
                print()
                if ("-" in lebar) or ("-" in luas):
                    print("Error: Tidak bisa melakukan input negatif.")
                elif ("." in lebar or lebar.isdigit()) and ("." in luas or luas.isdigit()):
                    try:
                        hasil = panjang_lebarluas(lebar, luas)
                        print("Panjang persegi panjang adalah: " + str(hasil))
                    except ZeroDivisionError or ValueError:
                        print("Error: Pembagian nol / input salah.")
                else:
                    print("Error: Kesalahan input.")
            elif pilihan == "a2":
                while not lebar:
                    lebar = input("Sisi lebar: ")
                while not keliling:
                    keliling = input("Keliling persegi panjang: ")
                print()
                if ("-" in lebar) or ("-" in keliling):
                    print("Error: Tidak bisa melakukan input negatif.")
                elif ("." in lebar or lebar.isdigit()) and ("." in keliling or keliling.isdigit()):
                    try:
                        hasil = panjang_lebarkeliling(lebar, keliling)
                        if hasil > 0:
                            print("Panjang persegi panjang adalah: " + str(hasil))
                        else:
                            print("Hasil invalid >> " + str(hasil))
                    except ValueError:
                        print("Error: Kesalahan input.")
                else:
                    print("Error: Kesalahan input.")
            elif pilihan == "b1":
                while not panjang:
                    panjang = input("Sisi panjang: ")
                while not luas:
                    luas = input("Luas persegi panjang: ")
                print()
                if ("-" in panjang) or ("-" in luas):
                    print("Error: Tidak bisa melakukan input negatif.")
                elif ("." in panjang or panjang.isdigit()) and ("." in luas or luas.isdigit()):
                    try:
                        hasil = lebar_panjangluas(panjang, luas)
                        print("Lebar persegi panjang adalah: " + str(hasil))
                    except ZeroDivisionError or ValueError:
                        print("Error: Pembagian nol / kesalahan input.")
                else:
                    print("Error: Kesalahan input.")
            elif pilihan == "b2":
                while not panjang:
                    panjang = input("Sisi panjang: ")
                while not keliling:
                    keliling = input("Keliling persegi panjang: ")
                print()
                if ("-" in panjang) or ("-" in keliling):
                    print("Error: Tidak bisa melakukan input negatif.")
                elif ("." in panjang or panjang.isdigit()) and ("." in keliling or keliling.isdigit()):
                    try:
                        hasil = lebar_panjangkeliling(panjang, keliling)
                        if hasil > 0:
                            print("Lebar persegi panjang adalah: " + str(hasil))
                        else:
                            print("Hasil invalid >> " + str(hasil))
                    except ValueError:
                        print("Error: Kesalahan input.")
                else:
                    print("Error. Kesalahan input")
            elif pilihan == "c1":
                while not panjang:
                    panjang = input("Sisi panjang: ")
                while not lebar:
                    lebar = input("Sisi lebar: ")
                print()
                if ("-" in panjang) or ("-" in lebar):
                    print('Error: Tidak bisa melakukan input negatif.')
                elif ("." in panjang or panjang.isdigit()) and ("." in lebar or lebar.isdigit()):
                    try:
                        hasil = diagonal_rectangle(panjang, lebar)
                        print("Diagonal persegi panjang adalah: " + str(hasil))
                    except ValueError:
                        print("Error: Kesalahan input.")
                else:
                    print("Error: Kesalahan input.")
            else:
                print("Error. kesalahan input.")
        else:
            print("Error. Kesalahan input")
        time.sleep(3)
        print()
        print("=== Eksekusi berhasil ===")
        print("=== def persegi_panjang is completed ===")
        repeat()
    # Bangun 2D: Segitiga [Need Bug Hunter ASAP]
    def segitiga():
        # Bagian implementasi rumus-rumus segitiga
        def luas_segitiga(alas, tinggi):
            alas, tinggi = float(alas), float(tinggi)
            luas = (alas * tinggi)/2
            return luas
        def keliling_segitiga(a, b, c):
            a, b, c = float(a), float(b), float(c)
            keliling = a + b + c
            return keliling
        # Bagian advanced
        def alas_tinggiluas(tinggi, luas):
            tinggi, luas = float(tinggi), float(luas)
            alas = (2 * luas)/tinggi
            return alas
            # Berpotensi zerodivisionerror
        def tinggi_alasluas():
            alas, luas = float(alas), float (luas)
            tinggi = (2 * luas)/alas
            return tinggi
            # Berpotensi zerodivisionerror
        def sudut_hilang(angle1, angle2):
            angle3 = 180 - (angle1 + angle2)
            return angle3
            # Berpotensi nilai negatif
            # Casting float di tampilan ui advanced
        #def khusus pythagoras
        def pythagoras_c(a, b):
            a = float(a)
            b = float(b)
            pre_result = math.pow(a, 2) + math.pow(b, 2)
            if pre_result > 0:
                panjang_c = math.sqrt(pre_result)
                return panjang_c
            else:
                print("(Error: Bilangan akar negatif)")
                return "[Error]"
        def pythagoras_a(c, b):
            b = float(b)
            c = float(c)
            pre_result = math.pow(c, 2) - math.pow(b, 2)
            if pre_result > 0:
                panjang_a = math.sqrt(pre_result)
                return panjang_a
            else:
                print("(Error: Bilangan akar negatif)")
                return "[Error]"
        def pythagoras_b(c, a):
            a = float(a)
            c = float(c)
            pre_result = math.pow(c, 2) - math.pow(a, 2)
            if pre_result > 0:
                panjang_b = math.sqrt(pre_result)
                return panjang_b
            else:
                print("(Error: Bilangan akar negatif)")
                return "[Error]"
        print(r"   __    ____    ____             _ _   _             ")
        print(r"  / /   / /\ \  / ___|  ___  __ _(_) |_(_) __ _  __ _ ")
        print(r" / /   / /  \ \ \___ \ / _ \/ _` | | __| |/ _` |/ _` |")
        print(r" \ \  / /   / /  ___) |  __/ (_| | | |_| | (_| | (_| |")
        print(r"  \_\/_/   /_/  |____/ \___|\__, |_|\__|_|\__, |\__,_|")
        print(r"                            |___/         |___/       ")
        print()
        print("=== Bangun Terpilih: Segitiga ===")
        print()
        print("Silahkan pilih mode untuk bangun Segitiga:")
        print("A = Menghitung luas segitiga")
        print("B = Menghitung keliling dengan sisi segitiga")
        print("C = Advanced")
        print()
        pilihan = None
        alas = None
        tinggi = None
        luas = None
        sisi_a = None
        sisi_b = None
        sisi_c = None
        angle1 = None
        angle2 = None
        sisi_miring = None
        sisi_tegak = None
        sisi_datar = None
        # While not pilihan tingkatan luar (Non-Advanced)
        while not pilihan:
            pilihan = input("Pilihan: ").lower()
        print()
        if pilihan == "a":
            while not alas:
                alas = input("Panjang alas: ")
            while not tinggi:
                tinggi = input("Panjang tinggi: ")
            print()
            if ("-" in alas) or ("-" in tinggi):
                print("Error: Tidak bisa melakukan input negatif.")
            elif ("." in alas or alas.isdigit()) and ("." in tinggi or tinggi.isdigit()):
                try:
                    hasil = luas_segitiga(alas, tinggi)
                    print ("Luas segitiga adalah: " + str(hasil))
                except ValueError:
                    print("Error: Kesalahan input.")
            else:
                print("Error: Kesalahan input.")
        elif pilihan =="b":
            while not sisi_a:
                sisi_a = input("Panjang sisi A: ")
            while not sisi_b:
                sisi_b = input("Panjang sisi B: ")
            while not sisi_c:
                sisi_c = input("Panjang sisi C: ")
            print()
            if ("-" in sisi_a) or ("-" in sisi_b) or ("-" in sisi_c):
                print("Error: Tidak bisa melakukan input negatif.")
            elif ("." in sisi_a or sisi_a.isdigit()) and ("." in sisi_b or sisi_b.isdigit()) and ("." in sisi_c or sisi_c.isdigit()):
                try:
                    hasil = keliling_segitiga(sisi_a, sisi_b, sisi_c)
                    print("Keliling segitiga adalah: " + str(hasil))
                except ValueError:
                    print("Error: Kesalahan input.")
            else:
                print("Error: Kesalahan input.")
        elif pilihan == "c":
            # Bagian tampilan terminal: Advanced
            print("=== Advanced: Segitiga ===")
            print()
            print("A = Mencari alas segitiga")
            print("B = Mencari tinggi segitiga")
            print("C = Menghitung sudut yg. hilang (diketahui dua sudut)")
            print("D = Mode Pythagoras")
            print()
            print("</> Trigonometri?, under development :)")
            print()
            # Menghapus isi var. pilihan agar bisa digunakan kembali
            pilihan = None
            while not pilihan:
                pilihan = input("Pilihan: ").lower()
            print()
            if pilihan == "a":
                while not tinggi:
                    tinggi = input("Panjang tinggi: ")
                while not luas:
                    luas = input("Luas segitiga: ")
                print()
                if ("-" in tinggi) or ("-" in luas):
                    print("Error: Tidak bisa melakukan input negatif.")
                elif ("." in tinggi or tinggi.isdigit()) and ("." in luas or luas.isdigit()):
                    try:
                        hasil = alas_tinggiluas(tinggi, luas)
                        print("Panjang alas segitiga adalah: " + str(hasil))
                    except ZeroDivisionError or ValueError:
                        print("Error: Pembagian nol / input salah.")
                else:
                    print("Error: Kesalahan input.")
            elif pilihan == "b":
                while not alas:
                    alas = input("Panjang alas: ")
                while not luas:
                    luas = input("Luas segitiga: ")
                print()
                if ("-" in alas) or ("-" in luas):
                    print("Error: Tidak bisa melakukan input negatif.")
                elif ("." in alas or alas.isdigit()) and ("." in luas or luas.isdigit()):
                    try:
                        hasil = tinggi_alasluas(alas, luas)
                        print("Panjang tinggi segitiga adalah: " + str(hasil))
                    except ZeroDivisionError or ValueError:
                        print("Error: Pembagian nol / input salah.")
                else:
                    print("Error: Kesalahan input.")
            elif pilihan == "c":
                while not angle1:
                    angle1 = input("Besar sudut pertama: ")
                while not angle2:
                    angle2 = input("Besar sudut kedua: ")
                print()
                if ("-" in angle1) or ("-" in angle2):
                    print("Error: Tidak bisa melakukan input negatif.")
                elif ("." in angle1 or angle1.isdigit()) and ("." in angle2 or angle2.isdigit()):
                    try:
                        angle1, angle2 = float(angle1), float(angle2)
                        try:
                            if (angle1 > 0) and (angle2 > 0):
                                hasil = sudut_hilang(angle1, angle2)
                                if hasil > 0 and hasil < 180:
                                    print("Besar sudut ketiga adalah: " + str(hasil))
                                else:
                                    # Apabila var. hasil kurang,sama dari 0 / melebiihi,sama dengan 180
                                    print("Error: Nilai melebihi 180 atau lebih kecil dari 0.")
                            else:
                                print("Error: Input nol.")
                        except ValueError:
                            print("Error: Kesalahan input.")
                    except ValueError:
                        print("Error: Kesalahan input")
                else:
                    print("Error: Kesalahan input.")
            elif pilihan =="d":
                print("=== Advanced: Segitiga >> Mode Pythagoras ===")
                print()
                print("C = Mencari sisi miring segitiga (Hipoterusa)")
                print("A = Mencari sisi tegak segitiga (Vertikal)")
                print("B = Mencari sisi datar segitiga (Horizontal)")
                print()
                pilihan = None
                while not pilihan:
                    pilihan = input("Pilihan: ").lower()
                print()
                if pilihan == "c":
                    while not sisi_tegak:
                        sisi_tegak = input("Sisi tegak segitiga (a): ")
                    while not sisi_datar:
                        sisi_datar = input("Sisi datar segitiga (b): ")
                    print()
                    if ("-" in sisi_tegak) or ("-" in sisi_datar):
                        print("Error: Tidak bisa melakukan input negatif.")
                    elif ("." in sisi_tegak or sisi_tegak.isdigit()) and ("." in sisi_datar or sisi_datar.isdigit()):
                        try:
                            hasil = pythagoras_c(sisi_tegak, sisi_datar)
                            print("Sisi miring segitiga adalah (c): " + str(hasil))
                        except ValueError:
                            print("Error: Kesalahan input.")
                    else:
                        print("Error: Kesalahan input")
                elif pilihan == "a":
                    while not sisi_miring:
                        sisi_miring = input("Sisi miring segitiga (c): ")
                    while not sisi_datar:
                        sisi_datar = input("Sisi datar segitiga (b): ")
                    print()
                    if ("-" in sisi_miring) or ("-" in sisi_datar):
                        print("Error: Tidak bisa melakukan input negatif.")
                    elif ("." in sisi_miring or sisi_miring.isdigit()) and ("." in sisi_datar or sisi_datar.isdigit()):
                        try:
                            hasil = pythagoras_a(sisi_miring, sisi_datar)
                            if not hasil  == "[Error]":
                                print("Sisi tegak segitiga adalah (a): " + str(hasil))
                        except ValueError:
                            print("Error: Kesalahan input.")
                    else:
                        print("Error: Kesalahan input.")
                elif pilihan == "b":
                    while not sisi_miring:
                        sisi_miring = input("Sisi miring segitiga (c): ")
                    while not sisi_tegak:
                        sisi_tegak = input("Sisi datar segitiga (a): ")
                    print()
                    if ("-" in sisi_miring) or ("-" in sisi_tegak):
                        print("Error: Tidak bisa melakukan input negatif.")
                    elif ("." in sisi_miring or sisi_miring.isdigit()) and ("." in sisi_tegak or sisi_tegak.isdigit()):
                        try:
                            hasil = pythagoras_b(sisi_miring, sisi_tegak)
                            if not hasil  == "[Error]":
                                print("Sisi datar segitiga adalah (b): " + str(hasil))
                        except ValueError:
                            print("Error: Kesalahan input.")
                    else:
                        print("Error: Kesalahan input.")
                else:
                    print("Error: Kesalahan input.")
            else:
                print("Error: Kesalahan input.")
        else:
            print("Error: Kesalahan input.")
        time.sleep(3)
        print()
        print("=== Eksekusi berhasil ===")
        print("</> def segitiga")
        repeat()
    # Bangun 2D: Lingkaran
    def lingkaran():
        r = None
        diameter = None
        luas = None
        keliling = None
        derajat = None
        pi = math.pi
        # def rumus-rumus umum (dengan jari)
        def luas_r(r):
            r = float(r)
            luas = pi * math.pow(r,2)
            return luas
        def keliling_r(r):
            r = float(r)
            keliling = 2 * pi * math.pow(r,2)
            return keliling
        # def rumus-rumus umum (dengan diameter)
        def luas_d(diameter):
            diameter = float(diameter)
            r = diameter / 2
            luas = pi * math.pow(r, 2)
            return luas
        def keliling_d(diameter):
            diameter = float(diameter)
            keliling = pi * diameter
            return keliling
        # def advanced
        # mencari r dan d
        def diameter_r(r):
            r = float(r)
            diameter = 2 * r
            return diameter
        def r_diameter(diameter):
            diameter = float(diameter)
            jari = diameter / 2
            return jari
        # mencari d dan r dari komponen luas atau keliling
        def r_luas(luas):
            luas = float(luas)
            jari = math.sqrt(luas / pi)
            return jari
        def r_keliling(keliling):
            keliling = float(keliling)
            jari = keliling / (2 * pi)
            return jari
        def d_luas (luas):
            luas = float(luas)
            diameter = math.sqrt((4 * luas) / pi)
            return diameter
        def d_keliling (keliling):
            keliling = float(keliling)
            diameter = keliling / pi
            return diameter
        # advanced: zona-zona
        def luas_zona(r, derajat):
            r = float(r)
            derajat = float(derajat)
            if 0 < derajat <= 360:
                luasz = (derajat / 360) * (pi * math.pow(r, 2))
                return luasz
            else:
                luasz = "invalid"
                return luasz
        def keliling_zona(r, derajat):
            r = float(r)
            derajat = float(derajat)
            kelilingz = (derajat/360) * (2 * pi * r)
            return kelilingz
        # advanced: cincin lingkaran
        def luascincin_lingkaran(rbig, rlil):
            rbig = float(rbig)
            rlil = float(rlil)
            cincin = (2 * pi * rbig) + (2 * pi * rlil)
            return cincin
        # Tampialn menu awal untuk kalkulator lingkaran
        print(r"  __    ____    _     _             _                         ")
        print(r" / /   / /\ \  | |   (_)_ __   __ _| | ____ _ _ __ __ _ _ __  ")
        print(r"/ /   / /  \ \ | |   | | '_ \ / _` | |/ / _` | '__/ _` | '_ \ ")
        print(r"\ \  / /   / / | |___| | | | | (_| |   < (_| | | | (_| | | | |")
        print(r" \_\/_/   /_/  |_____|_|_| |_|\__, |_|\_\__,_|_|  \__,_|_| |_|")
        print(r"                              |___/                           ")
        print()
        print("=== Bangun Terpilih: Lingkaran ===")
        print("Catatan: Menggunakan pi irasional -> " + str(pi))
        print()
        print("Silahkan pilih mode untuk bangun lingkaran.")
        print()
        print("</> DIKETAHUI JARI-JARI")
        print("A1 = Menghitung luas lingkaran")
        print("A2 = Menghitung keliling lingkaran")
        print()
        print("</> DIKETAHUI DIAMETER")
        print("B1 = Mengitung luas lingkaran")
        print("B2 = Menghitung keliling lingkaran")
        print()
        print("C = Advanced")
        print()
        pilihan = None
        while not pilihan:
            pilihan = input("Pilihan: ").lower()
        print()
        # Bagian out dan eksekusi
        # luas dan keliling menggunakan r
        if pilihan == "a1":
            while not r:
                r = input("Jari-jari lingkaran: ")
            print()
            if "-" in r:
                print("Error: Tidak bisa melakukan input negatif.")
            elif ("." in r or r.isdigit()):
                try:
                    hasil = luas_r(r)
                    if not hasil == 0:
                        print("Luas lingkaran adalah")
                        print()
                        print("Sebelum dibulatkan: " + str(hasil))
                        print("Sesudah dibulatkan: " + str(round(hasil)))
                    else:
                        print("Tidak bisa melakukan input nol.")
                except ValueError:
                    print("Error: Kesalahan input.")
            else:
                print("Error: Kesalahan input.")
        elif pilihan == "a2":
            while not r:
                r = input("Jari-jari lingkaran: ")
            print()
            if "-" in r:
                print("Error: Tidak bisa melakukan input negatif.")
            elif ("." in r or r.isdigit()):
                try:
                    hasil = keliling_r(r)
                    if not hasil == 0:
                        print("Keliling lingkaran adalah")
                        print()
                        print("Sebelum dibulatkan: " + str(hasil))
                        print("Sesudah dibulatkan: " + str(round(hasil)))
                    else:
                        print("Error: Tidak bisa melakukan input nol.")
                except ValueError:
                    print("Error: Kesalahan input")
            else:
                print("Error: Kesalahan input.")
        # luas dan keliling menggunakan diameter
        elif pilihan == "b1":
            while not diameter:
                diameter = input("Diameter lingkaran: ")
            print()
            if "-" in diameter:
                print("Error: Tidak bisa melakukan input negatif.")
            elif ("." in diameter or diameter.isdigit()):
                try:
                    hasil = luas_d(diameter)
                    if not hasil == 0:
                        print("Luas lingkaran adalah")
                        print()
                        print("Sebelum dibulatkan: " +str(hasil))
                        print("Sesudah dibulatkan: " + str(round(hasil)))
                    else:
                        print("Error: Tidak bisa melakukan input nol.")
                except ValueError:
                    print("Error: Kesalahan input.")
            else:
                print("Error: Kesalahan input.")
        elif pilihan =="b2":
            while not diameter:
                diameter = input("Diameter lingkaran: ")
            print()
            if "-" in diameter:
                print("Error: Tidak bisa melakukan input negatif.")
            elif ("." in diameter or diameter.isdigit()):
                try:
                    hasil = keliling_d(diameter)
                    if not hasil == 0:
                        print("Keliling lingkaran adalah")
                        print()
                        print("Sebelum dibulatkan: " + str(hasil))
                        print("Sesudah dibulatkan: " + str(round(hasil)))
                    else:
                        print("Error: Tidak bisa melakukan input nol.")
                except ValueError:
                    print("Error: Kesalahan input.")
            else:
                print("Error: Kesalahan input.")
        # opsi c untuk masuk bagian advanced (tingkatan lanjut)
        elif pilihan == "c":
            print("=== Advanced: Lingkaran ===")
            print()
            print("A1 = Mencari diameter dari jari-jari")
            print("A2 = Mencari jari-jari dari diameter")
            print()
            print("B1 = Mencari jari-jari dari luas lingkaran")
            print("B2 = Mencari jari-jari dari keliling lingkaran")
            print("B3 = Mencari diameter dari luas lingkaran")
            print("B4 = Mencari diameter dari keliling lingkaran")
            print()
            print("C1 = Mencari luas sebagian zona/bagian lingkaran")
            print("C2 = Mencari luas cincin dari dua lingkaran")
            print()
            pilihan = None
            while not pilihan:
                pilihan = input("Pilihan: ").lower()
            print()
            if pilihan == "a1":
                while not r:
                    r = input("Jari-jari lingkaran: ")
                print()
                if "-" in r:
                    print("Error: Tidak bisa melakukan input negatif.")
                elif "." in r or r.isdigit():
                    try:
                        hasil = diameter_r(r)
                        if not hasil == 0:
                            print("Diameter lingkaran adalah: " + str(hasil))
                        else:
                            print("Error: Tidak bisa melakukan input negatif.")
                    except ValueError:
                        print("Error: Kesalahan input.")
                else:
                    print("Error: Kesalahan input.")
            elif pilihan == "a2":
                while not diameter:
                    diameter = input("Diameter lingkaran: ")
                print()
                if "-" in diameter:
                    print("Error: Tidak bisa melakukan input negatif.")
                elif "." in diameter or diameter.isdigit():
                    try:
                        hasil = r_diameter(diameter)
                        if not hasil == 0:
                            print("Jari-jari lingkaran adalah: " + str(hasil))
                        else:
                            print("Error: Tidak bisa melakukan input nol.")
                    except ValueError:
                        print("Error: Kesalahan input.")
                else:
                    print("Error: Kesalahan input.")
            # B1 sampai B4
            elif pilihan == "b1":
                while not luas:
                    luas = input("Luas lingkaran: ")
                print()
                if "-" in luas:
                    print("Error: Tidak bisa melakukan input negatif.")
                elif "." in luas or luas.isdigit():
                    try:
                        hasil = r_luas(luas)
                        if not hasil == 0:
                            print("Jari-jari lingkaran adalah: " + str(hasil))
                        else:
                            print("Error: Tidak bisa melakukan input nol.")
                    except ValueError:
                        print("Error: Kesalahan input.")
                else:
                    print("Error: Kesalahan input.")
            elif pilihan == "b2":
                while not keliling:
                    keliling = input("Keliling lingkaran: ")
                print()
                if "-" in keliling:
                    print("Error: Tidak bisa melakukan input negatif.")
                elif "." in keliling or keliling.isdigit():
                    try:
                        hasil = r_keliling(keliling)
                        if not hasil == 0:
                            print("JAri-jari lingkaran adalah: " + str(hasil))
                        else:
                            print("Error: Tidak bisa melakukan input negatif.")
                    except ValueError:
                        print("Error: Kesalahan input.")
                else:
                    print("Error: Kesalahan input.")
            elif pilihan == "b3":
                while not luas:
                    luas = input("Luas lingkaran: ")
                print()
                if "-" in luas:
                    print("Error: Tidak bisa melakukan input negatif.")
                elif "." in luas or luas.isdigit():
                    try:
                        hasil = d_luas(luas)
                        if not hasil == 0:
                            print("Diameter lingkaran adalah: " + str(hasil))
                        else:
                            print("Error: Tidak bisa melakukan input nol.")
                    except ValueError:
                        print("Error: Kesalahan input.")
                else:
                    print("Error: Kesalahan input.")
            elif pilihan == "b4":
                while not keliling:
                    keliling = input("Keliling lingkaran: ")
                print()
                if "-" in keliling:
                    print("Error: Tidak bisa melakukan input negatif.")
                elif "." in keliling or keliling.isdigit():
                    try:
                        hasil = d_keliling(keliling)
                        if not hasil == 0:
                            print("Diameter lingkaran adalah: " + str(hasil))
                        else:
                            print("Error: Tidak bisa melakukan input nol.")
                    except ValueError:
                        print("Error: Kesalahan input.")
                else:
                    print("Error: Kesalahan input")
            #c1 sampai c2 (c3 seterusnya under development)
            elif pilihan == "c1":
                while not r:
                    r = input("Jari-jari lingkaran: ")
                while not derajat:
                    derajat = input("Besar zona dalam sudut derajat lingkaran (0 ~ ??): ")
                print()
                if ("-" in r) or ("-" in derajat):
                    print("Error: Tidak bisa melakukan iinput negatif.")
                elif ("." in r or r.isdigit()) and ("." in derajat or derajat.isdigit()):
                    try:
                        hasil = luas_zona(r, derajat)
                        if not hasil == "invalid":
                            print("Luas zona/sebagian lingkaran adalah: " + str(hasil))
                        else:
                            print("Error: Input derajat melebihi dari 360 atau tepat/kurang dari 0.")
                    except ValueError:
                        print("Error: Kesalahan input.")
                    
        # Masuk bagian advanced
                
        
        
    # Home menu >> Eksekusi awal dari main()
    print(r"  _  __     _ _          _       _                                ")
    print(r" | |/ /__ _| | | ___   _| | __ _| |_ ___  _ __                    ")
    print(r" | ' // _` | | |/ / | | | |/ _` | __/ _ \| '__|                   ")
    print(r" | . \ (_| | |   <| |_| | | (_| | || (_) | |                      ")
    print(r" |_|\_\__,_|_|_|\_\\__,_|_|\__,_|\__\___/|_|        _             ")
    print(r" | __ )  __ _ _ __   __ _ _   _ _ __   |  _ \  __ _| |_ __ _ _ __ ")
    print(r" |  _ \ / _` | '_ \ / _` | | | | '_ \  | | | |/ _` | __/ _` | '__|")
    print(r" | |_) | (_| | | | | (_| | |_| | | | | | |_| | (_| | || (_| | |   ")
    print(r" |____/ \__,_|_| |_|\__, |\__,_|_| |_| |____/ \__,_|\__\__,_|_|   ")
    print(r" __   _/ | / _ \    |___/                                         ")
    print(r" \ \ / / || | | |                                                 ")
    print(r"  \ V /| || |_| |                                                 ")
    print(r"  _\_(_)_(_)___/     _          _                        __       ")
    print(r" | _| ____|__ _ _ __| |_   _   / \   ___ ___ ___  ___ __|_ |      ")
    print(r" | ||  _| / _` | '__| | | | | / _ \ / __/ __/ _ \/ __/ __| |      ")
    print(r" | || |__| (_| | |  | | |_| |/ ___ \ (_| (_|  __/\__ \__ \ |      ")
    print(r" | ||_____\__,_|_|  |_|\__, /_/   \_\___\___\___||___/___/ |      ")
    print(r" |__|                  |___/                            |__|      ")
    print()
    print("=== Tampilan EarlyAccess ===")
    print()
    print("A = def persegi")
    print("B = def persegi_panjang")
    print('C = def segitiga')
    print("D = def lingkaran (under development)")
    print()
    pilihan = None
    while not pilihan:
        pilihan = input("Pilihan: ").lower()
    print()
    # Memanggil fungsi dengan input
    os.system("cls")
    if pilihan == "a":
        persegi()
    elif pilihan == "b":
        persegi_panjang()
    elif pilihan == "c":
        segitiga()
    elif pilihan =="d":
        lingkaran()
    else:
        print("Invalid input.")
# definisi pengulangan program/script >> memanggil lagi main() apabila true
def repeat():
    print()
    out = input("Ulangi? (y=ya), (n=tidak): ")
    if out == "y":
        os.system("cls")
        main()
    elif out == "n":
        os.system("cls")
        print("Terimakasih telah menggunakan program ini :)")
        time.sleep(3)
        
        print()
        print("<script_root> Eksekusi repeat berhasil >> (n)")
        exit()
    else:
        repeat()
        """
        Panggil definisi ini setiap setelah definisi
        suatu bangun berakhir dengan: eksekusi berhasil
        """
# Memanggil def utama agar script berjalan untuk eksekusi pertamanya
main()

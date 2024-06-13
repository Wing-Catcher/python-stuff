"""
Pesan untuk diri sendiri:
Keep up bro, pantang menyerah. Kita bisa bikin ini:
Kalkator Bangun Datar Umum
:)

Notes (Taruh disini)
- selalu konversi ke float, support desimal, dan returning point
"""
import math
import time
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
    #Bagian tampilan terminal
    print("=== Bangun Terpilih: Persegi ===")
    print()
    print("Silahkan pilih mode untuk bangun persegi:")
    print("A = Mencari luas persegi")
    print("B = Mencari keliling persegi")
    print("C = Mencari sisi dari diketahui luas")
    print("D = Mencari sisi dari diketahui keliling")
    print()
    pilihan = None
    while not pilihan:
        pilihan = input("Pilihan: ").lower()
    print()
    if pilihan == "a":
        sisi = None
        while not sisi:
            sisi = input("Sisi persegi: ")
        if "-" in sisi:
            print("Error: Tidak bisa melakukan input negatif.")
            time.sleep(3)
        elif "." in sisi or sisi.isdigit():
            try:
                hasil = luas_persegi(sisi)
                print()
                print("Luas persegi adalah: " + str(hasil))
                time.sleep(3)
            except ValueError:
                print("Error: Kesalahan input.")
                time.sleep(3)
        else:
            print("Error: Kesalahan input.")
            time.sleep(3)
    elif pilihan == "b":
        sisi = None
        while not sisi:
            sisi = input("Sisi persegi: ")
        if "-" in sisi:
            print("Error: Tidak bisa melakukan input negatif.")
            time.sleep(3)
        elif "." in sisi or sisi.isdigit():
            try:
                hasil = keliling_persegi(sisi)
                print()
                print("Keliling persegi adalah: " + str(hasil))
                time.sleep(3)
            except ValueError:
                print("Error: Kesalahan input.")
                time.sleep(3)
        else:
            print("Error: Kesalahan input.")
            time.sleep(3)
    elif pilihan == "c":
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
                time.sleep(3)
            except ValueError:
                print("Error. Kesalahan input.")
                time.sleep(3)
        else:
            print("Error: Kesalahan input.")
    elif pilihan == "d":
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
                time.sleep(3)
            except ValueError:
                print("Error. Kesalahan input.")
                time.sleep(3)
        else:
            print("Error: Kesalahan input.")
    else:
        print("Error. Kesalahan input.")
    print()
    print("=== Eksekusi sukses ===")
    print("=== DEBUG: exit code 0 ===")
# Bangun 2D Persegi Panjang
def persegi_panjang():
    #Bagian implementasi rumus dengan float casting
    def luas_persegi_panjang(panjang, lebar):
         panjang, lebar = float(panjang), float(lebar)
         luas = panjang * lebar
         return luas
    def keliling_persegi_panjang(panjang,lebar):
        panjang, lebar = float(panjang), float(lebar)
        keliling = 2 * (panjang*lebar)
        return keliling
    def panjang_persegipanjnag_dari_luaslebar(luas, lebar):
        # Zerodivision error dibagian UI
        luas, lebar = float(luas), float(lebar)
        panjang = luas / lebar
        return panjang
    def panjang_persegipanjnag_dari_kellebar(keliling, lebar):
        keliling, lebar = float(keliling), float(lebar)
        panjang = (keliling - lebar)/2
        return panjang
    def lebar_persegipanjnag_dari_luaspanjang(luas, panjang):
        # Zerodivision error dibagian UI
        luas, panjang = float(luas), float(panjang)
        lebar = luas / panjang
        return lebar
    def lebar_persegipanjnag_dari_kelpanjang(keliling, panjang):
        keliling, panjang = float(keliling), float(panjang)
        lebar = (keliling - panjang)/2
        return lebar
    #Bagian tampilan terminal
    print("=== Bangun Terpilih: Persegi Panjang")
    print()
    print("Silahkan pilih mode untuk Persegi Panjang")
    print("A = Mencari luas persegi panjang")
    print("B = Mencari keliling persegi panjang")
    print("C = Advanced")
    print()
    pilihan = None
    while not pilihan:
        pilihan = input("Pilihan: ").lower()
    print()
    if pilihan == "a":
        panjang = None
        while not panjang:
            panjang = input("Panjang persegi panjang: ")
        lebar = None
        while not lebar:
            lebar = input("Lebar peres")
persegi()
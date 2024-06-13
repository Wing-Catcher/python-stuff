"""
Lets we rewind back to our first language we learn
Python
"""
import math
import time
import os
def main():
    os.system("cls")
    def persegi():
        def luas_persegi(lebar, panjang):
            lebar, panjang = float(lebar), float(panjang)
            luas = lebar * panjang
            return luas
        def keliling_persegi(lebar, panjang):
            lebar, panjang = float(lebar), float(panjang)
            keliling = (lebar + panjang)*2
            return keliling
        print("=== Bangun terpilih: Persegi ===")
        print()
        print("Pilih mode untuk persegi")
        print("1 = mencari luas persegi")
        print("2 = mencari keliling persegi")
        print()
        pilihan = None
        while not pilihan:
            pilihan = input("Pilihan: ").lower()
        print()
        if pilihan == "1":
            panjang, lebar = None, None
            while not panjang:
                panjang = input("Panjang persegi: ")
            while not lebar:
                lebar = input("Lebar persegi")
            print()
            if ("-" in panjang) or ("-" in lebar):
                print("Error: Tidak bisa melakukan input negatif")
            elif ("." in panjang or panjang.isdigit()) and ("." in lebar or lebar.isdigit()):
                try:
                    hasil = luas_persegi(lebar, panjang)
                    print("Luas persegi adalah: " + str(hasil))
                except ValueError:
                    print("Error: Kesalahan input.")
            else:
                print("Error: Kesalahan input")
        else:
            print("Error: Kesalahan input")
    print("=== Silahkan pilih bangun yang ingin dihitung:")
    print("1 = persegi")
    print()
    pilihan = None
    while not pilihan:
        pilihan = input("Pilihan: ").lower()
    if pilihan == "1":
        persegi()
    else:
        print("Error input")
main()
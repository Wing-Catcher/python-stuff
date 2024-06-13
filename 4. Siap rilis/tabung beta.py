'''
Project kalkulator tabung by wing
Unreleased beta
'''
import math
import time
print("==============================")
print("Selamat datang di kalkulator Tabung")
print("Versi awal beta")
print("v.1.0 (beta)")
print("Menggunakan Pi Irasional >> " + str(math.pi))
print()
print("Tips: Gunakan titik '.' untuk memasukkan nilai desimal.")
print("==============================")
time.sleep(1.5)
pi = math.pi
print()
print("Silahkan pilih mode: ")
print("a = Mencari Volume")
print("b = Mencari Luas permukaan")
print("c = Extra")
print()
pilihan = None
while not pilihan:
    pilihan = input("Pilihan: ").lower()
if pilihan == "a":
    print()
    jari = None
    tinggi = None
    while not jari:
        jari = input("Masukkan Jari-jari: ")
    while not tinggi:
        tinggi = input("Masukkan Tinggi: ")
    if ("." in jari or jari.isdigit())and("." in tinggi or tinggi.isdigit()):
        jari, tinggi = float(jari), float(tinggi)
        vol = pi * math.pow(jari,2) * tinggi
        print()
        print("(Belum bulat) >> "+ str(vol))
        print("(Setelah dibulatkan) >> " + str(round(vol)))
        time.sleep(3)
    elif ("." in jari or "-" in jari or jari.isdigit())and("." in tinggi or "-" in tinggi or tinggi.isdigit()):
        print()
        print("Tidak bisa melakukan input minus")
        time.sleep(3)
    else:
        print()
        print("Kesalahan input. Error")
        time.sleep(3)
elif pilihan == "b":
    print()
    jari = None
    tinggi = None
    while not jari:
        jari = input("Masukkan Jari-jari: ")
    while not tinggi:
        tinggi = input("Masukkan tinggi: ")
    if ("." in jari or jari.isdigit())and("." in tinggi or tinggi.isdigit()):
        jari, tinggi = float(jari), float(tinggi)
        lp = 2 * pi * jari * (jari + tinggi)
        print()
        print("(Sebelum dibulatkan) >> " +str(lp))
        print("(Setelah dibulatkan) >> " + str(round(lp)))
        time.sleep(3)
    elif ("." in jari or "-" in jari or jari.isdigit())and("." in tinggi or "-" in tinggi or tinggi.isdigit()):
        print()
        print("Tidak bisa melakukan input minus.")
        time.sleep(3)
    else:
        print()
        print("Kesalahan  input.")
        time.sleep(3)
elif pilihan == "c":
    print()
    print("=== Extra ===")
    print("a = Mencari luas permukaan dan keliling dari selimut")
    print("b = Mencari luas permukaan dan keliling alas")
    print("c = Mode Kerucut")
    print("d = Rumus")
    print()
    pilihan1 = None
    while not pilihan1:
        pilihan1 = input("Pilihan: ").lower()
    if pilihan1 == "a":
        jari = None
        tinggi = None
        while not jari:
            jari = input("Jari-jari: ")
        while not tinggi:
            tinggi = input("Tinggi: ")
        if ("." in jari or jari.isdigit())and("." in tinggi or tinggi.isdigit()):
            try:
                jari, tinggi = float(jari) , float(tinggi)
                lpselimut = (2 * pi * jari)*tinggi
                kselimut = 2 * ((2 * pi *jari) + tinggi)
                print()
                print("=== Luas Permukaan Selimut ===")
                print("(Sebelum dibulatkan) >> " + str(lpselimut))
                print("(Setelah dibulatkan) >> " + str(round(lpselimut)))
                time.sleep(1)
                print("=== Keliling Selimut ===")
                print("(Sebelum dibulatkan) >>> " + str(kselimut))
                print("(Setelah dibulatkan) >>> " + str(round(kselimut)))
                time.sleep(3)
            except ValueError:
                print("Kesalahan input. Cek kembali input anda")
                time.sleep(3)
        elif ("." in jari or "-" in jari or jari.isdigit())and("." in tinggi or "-" in tinggi or tinggi.isdigit()):
            print("Tidak bisa melakukan input negatif.")
            time.sleep(3)
        else:
            print("Kesalahan input.")
            time.sleep(3)
    elif pilihan1 == "b":
        jari = None
        while not jari:
            jari = input("Jari-jari: ").lower()
        if "." in jari or jari.isdigit():
            try:
                jari = float(jari)
                lpalas = pi * math.pow(jari,2)
                kelalas = 2 * pi * jari
                print()
                print("=== Luas Permukaan Alas ===")
                print("(Sebelum dibulatkan) >>> " + str(lpalas))
                print("(Sesudah dibulatkan) >>> " + str(round(lpalas)))
                time.sleep(1)
                print("=== Keliling Alas ===")
                print("(Sebelum dibulatkan) >>> " + str(kelalas))
                print("(Setelah dibulatkan) >>> " + str(round(kelalas)))
                time.sleep(3)
            except ValueError:
                print("Kesalahan input. Cek kembali input anda.")
        elif "." in jari or "-" in jari or jari.isdigit():
            print("Tidak bisa melakukan input negatif.")
            time.sleep(3)
        else:
            print("Kesalahan input.")
            time.sleep(3)
    elif pilihan1 =="c":
        print()
        print("=== Mode Kerucut ===")
        print()
        print("Pilih mode: ")
        print("a = Mencari Volume Kerucut")
        print("b = Mencari Luas Permukaan Kerucut")
        print()
        pilihan2 = None
        while not pilihan2:
            pilihan2 = input("Pilihan: ").lower()
        if pilihan2 == "a":
            jari = None
            tinggi = None
            while not jari:
                jari = input("Jari-jari: ")
            while not tinggi:
                tinggi = input("Tinggi: ")
            print()
            if ("." in jari or jari.isdigit()) and ("." in tinggi or tinggi.isdigit()):
                try:
                    jari, tinggi = float(jari), float(tinggi)
                    volume = (pi * math.pow(jari,2) * tinggi)/3
                    print("(Sebelum dibulatkan) >>> " + str(volume))
                    print("(Setelah dibulatkan) >>> " + str(round(volume)))
                    time.sleep(3)
                except ValueError:
                    print("Kesalahan input.")
                    time.sleep(3)
            elif ("." in jari or "-" in jari or jari.isdigit()) and ("." in tinggi or "-" in tinggi or tinggi.isdigit()):
                print("Tidak bisa melakukan input negatif")
                time.sleep(3)
            else:
                print("Kesalahan input.")
        elif pilihan2 == "b":
            lukis = None
            jari = None
            tinggi = None
            while not lukis:
                lukis = input("Garis pelukis kerucut: ")
            while not jari:
                jari = input("Jari-jari: ")
            while not tinggi:
                tinggi = input("tinggi: ")
            print()
            if ("." in lukis or lukis.isdigit()) and ("." in jari or jari.isdigit()) and ("." in tinggi or tinggi.isdigit()):
                try:
                    lukis, jari, tinggi = float(lukis), float(jari), float(tinggi)
                    lpkerucut = pi * jari * (jari + lukis)
                    print("(Sebelum dibulatkan) >>> " + str(lpkerucut))
                    print("(Setelah dibulatkan) >>> " + str(round(lpkerucut)))
                    time.sleep(3)
                except ValueError:
                    print("Kesalahan input.")
                    time.sleep(3)
            elif ("." in lukis or "-" in lukis or lukis.isdigit()) and ("." in jari or "-" in jari or jari.isdigit()) and ("." in tinggi or "-" in tinggi or tinggi.isdigit()):
                print("Tidak bisa melakukan input negatif.")
                time.sleep(3)
            else:
                print("Kesalahan input.")
                time.sleep(3)
    elif pilihan1 == "d":
        print()
        print("=== Rumus ===")
        print()
        print("1. Tabung")
        print("     Volume                  = pi x r^2 x t")
        print("     Luas permukaan          = 2 x pi x r x (r + t)")
        print("     lp selimut              = (2 x pi x r) x tinggi")
        print("     Keliling selimut        = 2 x ((2 x pi x r) + t)")
        print("     lp alas                 = pi x r^2")
        print("     Keliling alas           = 2 x pi x jari")
        time.sleep(1)
        print()
        print("2. Kerucut")
        print("     Volume                  = (pi x r^2 x t) / 3")
        print("     lp kerucut              = pi x r x (r + Garis Pelukis atau 's')")
        time.sleep(3)
    else:
        print("Kesalahan input.")
        time.sleep(3)
else:
    print()
    print("Kesalahan input. Error")
    time.sleep(3)
"""
Tentang project ini

Kalulator tabung sederhana + kerucut
dengan penambahan fitur dari project-project sebelumnya
Target keberhasilan:

1. Menggunakan time.sleep
2. Desimal didukung
3. Antisipasi error dengan try except
4. Penyederhanaan kode
5. Penghapusan repeat modul

Coded and written by: @wingcatcher
"""
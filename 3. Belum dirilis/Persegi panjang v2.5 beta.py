# Kalkulator Persegi Panjang 2.5 BETA
import time
print("=============================")
print("Kalkulator Persegi Panjang 2.5 beta")
print("=============================")
print()
print("Pilih mode: ")
print("a = Menghitung Luas")
print("b = Menghitung Keliling")
print("c = Mencari Komponen")
print("d = Target BETA")
print("Comingsoon")
print()
pilihan = None
while not pilihan:
    pilihan = input("Pilihan: ").lower()
if pilihan == "a":
    panjang, lebar = None, None
    while not panjang:
        panjang = input("Diketahui Panjang: ")
    while not lebar:
        lebar = input("Diketahui Lebar: ")
    if ("." in panjang or "-" in panjang or panjang.isdigit()) and ("." in lebar or "-" in lebar or lebar.isdigit()):
        try:
            panjang, lebar = float(panjang), float(lebar)
            luas = panjang * lebar
            if luas >=0:
                print()
                print("Hasil luas adalah: "+ str(luas))
                time.sleep(3)
            elif luas <=0:
                print()
                print("Hasil invalid =>> " + str(luas) + " Cek kembali input anda.")
        except ValueError:
            print()
            print("Error Detected")
            time.sleep(3)
    else:
        print("Input except number detected. fail")
        time.sleep(3)
elif pilihan == "b":
    panjang, lebar = None, None
    while not panjang:
        panjang = input("Diketahui Panjang: ")
    while not lebar:
        lebar = input("Diketahui Lebar: ")
    if ("." in panjang or "-" in panjang or panjang.isdigit()) and ("." in lebar or "-" in lebar or lebar.isdigit()):
        try:
            panjang, lebar = float(panjang), float(lebar)
            keliling = 2*(panjang + lebar)
            if keliling >=0:
                print()
                print("Hasil keliling adalah: "+ str(keliling))
                time.sleep(3)
            elif keliling <=0:
                print()
                print("Hasil invalid =>> " + str(keliling) + " Cek kembali input anda.")
        except ValueError:
            print()
            print("Error Detected")
            time.sleep(3)
    else:
        print("Input except number detected. fail")
        time.sleep(3)
elif pilihan == "c":
    print()
    print("Komponen: ")
    print("a = Mencari panjang dari lebar dan luas")
    print("b = Mencari panjang dari lebar dan keliling")
    print("=========")
    print("c = Mencari lebar dari panjang dan luas")
    print("d = Mencari lebar dari panjang dan keliling")
    print()
    choose = None
    while not choose:
        choose = input("Pilihan: ").lower()
    print()
    if choose == "a":
        lebar = None
        luas = None
        while not lebar:
            lebar = (input("Lebar: "))
        while not luas:
            luas = (input("Luas: "))
        if ("." in lebar or lebar.isdigit()) and ("." in luas or luas.isdigit()):
            try:
                lebar, luas = float(lebar), float(luas)
                panjang = luas/lebar
                print("Panjang adalah: " + str(panjang))
                time.sleep(3)
            except ZeroDivisionError:
                print("Error, Tidak bisa pembagian dengan nol.")
                time.sleep(3)
            except ValueError:
                print("Error, Kesalahan input.")
                time.sleep(3)
        elif ("." in lebar or "-" in lebar or lebar.isdigit()) and ("." in luas or "-" in luas or luas.isdigit()):
            print()
            print("Input negatif tidak bisa dilakukan.")
            time.sleep(3)
        else:
            print("Error, kesalahn input")
    elif choose == "b":
        lebar = None
        keliling = None
        while not lebar:
            lebar= input("Lebar: ").lower()
        while not keliling:
            kelilig = input("Keliling: ").lower()
        if ("." in lebar or lebar.isdigit()) and ("." in keliling or keliling.isdigit()):
            try:
                lebar, keliling = float(lebar), float(keliling)
                panjang = (keliling/2)-lebar
                print("Panjang adalah: "+str(panjang))
                time.sleep(3)
            except ValueError:
                print("Error, Kesalahan input.")
                time.sleep(3)
            except ZeroDivisionError:
                print("Tidak bisa membagikan dengan nol")
        elif ("." in lebar or "-" in lebar or lebar.isdigit()) and ("." in keliling or "-" in keliling or keliling.isdigit()):
            print("Error, Tidak bisa melakukan operasi negatif")
            time.sleep(3)
        else:
            print("Error, Kesalahn input.")
            time.sleep(3)
    elif choose == "c":
        panjang = None
        luas = None
        while not panjang:
            panjang = (input("Panjang: "))
        while not luas:
            luas = (input("Luas: "))
        if ("." in panjang or panjang.isdigit()) and ("." in luas or luas.isdigit()):
            try:
                panjang, luas = float(panjang), float(luas)
                Lebar = luas/panjang
                print("Lebar adalah: " + str(Lebar))
                time.sleep(3)
            except ZeroDivisionError:
                print("Error, Tidak bisa pembagian dengan nol.")
                time.sleep(3)
            except ValueError:
                print("Error, Kesalahan input.")
                time.sleep(3)
        elif ("." in panjang or "-" in panjang or panjang.isdigit()) and ("." in luas or "-" in luas or luas.isdigit()):
            print()
            print("Input negatif tidak bisa dilakukan.")
            time.sleep(3)
        else:
            print("Error, kesalahan input")
elif pilihan == "d":
    print("1. Support Desimal")
    print("2. Looping ketika input kosong")
    print("3. Program selesai diakhiri sleep 3 detik")
    print("4. Menganggap semua bangun yang sama, output print persegi dihapus")
    time.sleep(3)
else:
    print("Input except a/b/c detected. fail")
    time.sleep(3)
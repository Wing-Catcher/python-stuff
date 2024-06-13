# Project membuat kalkulator lingkaran
import math
def restart():
    ulang = input("Apakah anda ingin mengulang? (y/n)").lower()
    if ulang == "y":
        start()
    elif ulang == "n":
        exit()
    else:
        input("Input selain y/n terdeteksi. klik enter untuk keluar")
def start():
    print("Access Granted!")
    print("Selamat datang di program kalkulator lingkaran")
    print("Dikode dan dibuat oleh: Raffy")
    print("* Tidak mendukung bilangan desimal")
    print()
    # tanda step 1
    print("Daftar mode kalkulator: ")
    print("a Lingkaran 2D (beta)")
    print("b Bola (beta)")
    pilihan = input("Pilihan: ").lower()
    if pilihan == "a":
        # pilihan a
        print()
        print("Silahkan pilih mode kalkulator untuk lingkaran: ")
        print("a Keliling lingkaran")
        print("b Luas lingkaran")
        print("Mencari komponen (masih pengembangan)")
        print()
        choice = input("Pilihan: ").lower()
        if choice == "a":
            print()
            print('  OOOOO')
            print(' O     O')
            print('O       O')
            print('O       O')
            print(' O     O')
            print('  OOOOO')
            print()
            r = input("Jari jari yang diketahui: ")
            # implementasi lingkaran
            if r.isdigit():
                r = float(r)
                keliling = 2*3.14*r
                input("Klik enter untuk menampilkan hasil.")
                print()
                print("Keliling lingkaran adalah: " + str(keliling) + ".")
                input("Program selesai, klik entar untuk keluar")
                restart()
            else:
                input("Input desimal/selain angka terdeteksi. Klik enter untuk keluar")
                restart()
        elif choice == "b":
            print()
            print('  OOOOO')
            print(' O     O')
            print('O       O')
            print('O       O')
            print(' O     O')
            print('  OOOOO')
            print()
            r = input("Jari jari yang diketahui: ")
            # implementasi lingkaran
            if r.isdigit():
                r = float(r)
                luas = 2 *3.14* math.pow(r,2)
                input("Klik enter untuk menampilkan hasil.")
                print()
                print("Luas lingkaran adalah: " + str(luas) + ".")
                input("Program selesai, klik entar untuk keluar")
                restart()
            else:
                input("Input desimal/selain angka terdeteksi. Klik enter untuk keluar")
                restart()
        else:
            input("Input selain a/b terdeteksi. Klik enter untuk keluar")
    elif pilihan == "b":
        # eksekusi mnghitung bangun bola ruang
        print()
        print("Silahkan pilih mode kalkulator untuk bangun lingkaran: ")
        print("a Volume lingkaran")
        print("b Luas permukaa lingkaran")
        print()
        choice = input("Pilihan: ").lower()
        if choice =="a":
            r = input("Jari-jari yang diketahui: ")
            if r.isdigit():
                r = float(r)
                luasbola = (4 * 3.14 * math.pow(r,3))/3
                input("Klik enter untuk menampilkan hasil.")
                print()
                print("Volume bola adalah: " + str(luasbola) + "*kubik")
                input("Klik enter untuk keluar.")
                ulang = input("Apakah anda ingin mengulang? (y/n)").lower()
                if ulang == "y":
                    start()
                else:
                    input("Input selain y/n terdeteksi. klik enter untuk keluar")
            else:
                input("Input desimal/huruf terdeteksi, Klik enter untuk keluar.")
                ulang = input("Apakah anda ingin mengulang? (y/n)").lower()
                if ulang == "a":
                    start()
                else:
                    input("Input selain y/n terdeteksi. klik enter untuk keluar")
        elif choice == "b":
            r = input("Jari-jari yang diketahui: ")
            if r.isdigit():
                r = float(r)
                luasp = 4 * 3.14 * math.pow(r,2)
                input("Klik enter untuk menampilkan hasil.")
                print()
                print("Luas permukaan bola adalah: " + str(luasp) + "*persegi")
                input("Klik enter untuk keluar")
                ulang = input("Apakah anda ingin mengulang? (y/n)").lower()
                if ulang == "a":
                    start()
                else:
                    input("Input selain y/n terdeteksi. klik enter untuk keluar")
            else:
                input("Input desimal/huruf terdeteksi. Klik enter untuk keluar.")
                ulang = input("Apakah anda ingin mengulang? (y/n)").lower()
                if ulang == "a":
                    start()
                else:
                    input("Input selain y/n terdeteksi. klik enter untuk keluar")
        else:
            input("Input a/b terdeteksi. Klik enter untuk keluar")
            ulang = input("Apakah anda ingin mengulang? (y/n)").lower()
            if ulang == "a":
                start()
            else:
                input("Input selain y/n terdeteksi. klik enter untuk keluar")
    else:
        input("Input selain a/b terdeteksi. Klik enter untuk keluar")
        ulang = input("Apakah anda ingin mengulang? (y/n)").lower()
        if ulang == "a":
            start()
        else:
            input("Input selain y/n terdeteksi. klik enter untuk keluar")
start()


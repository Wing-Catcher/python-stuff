# project membuat kalkulator again...
print("Selamat datang di kalkulator 2 digit")
print()
print("Silahkan isi digit pertama dan kedua")
digit_1 = input("digit pertama: ")
digit_2 = input("digit kedua: ")

print()

# eksekusi
if digit_1.isdigit() and digit_2.isdigit():
    digit_1 = int(digit_1)
    digit_2 = int(digit_2)
    #formulas
    sum = digit_1 + digit_2
    min = digit_1 - digit_2
    kali = digit_1 * digit_2
    if digit_2 == 0:
        bagi = "Tidak terdefinisi"
    else:
        bagi = digit_1 / digit_2
    print("Silahkan pilih operasi hitung:")
    print("a penjumlahan")
    print("b pengurangan")
    print("c perkalian")
    print("d pembagian")
    print()
    pilihan = input("Pilihan: ").lower()
    if pilihan == "a":
        print("Hasil pejumlahannya adalah: " + str(sum))
    elif pilihan == "b":
        print("hasil pengurangannya adalah: " + str(min))
    elif pilihan == "c":
        print("hasil perkaliannya adalah: " + str(kali))
    elif pilihan == "d":
        print("Hasil pembagiannya adalah: " + str(bagi))
    else:
        print("Input yang anda masukkan salah. menghentikan python")
else:
    print("input selain angka terdeteksi. menghentikan python")

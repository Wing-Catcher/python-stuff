import math
print("Selamat di project Kalkulator lingkaran")
print("* Tidak mendukung input desimal, hanya bilangan bulat")
print()
print("Silahkan metode hitung: ")
print("a Luas lingkaran")
print("b Keliling lingkaran")
print()
pilihan = input("Pilihan: ").lower()
if pilihan == "a":
    r = input("Masukkan jari jari lingkaran yang diketahui: ")
    if r.isdigit():
        r = float(r)
        luas = math.pi * (math.pow(r,2))
        print("Luas lingkaran adalah: " + str(luas) + " persegi")
    else:
        print("Input selain angka, desimal terdeteksi. mengehentikan python")
elif pilihan == "b":
    r = input("Masukkan jari jari lingkaran yang diketahui: ")
    if r.isdigit():
        r = float(r)
        d = r+r
        keliling = math.pi * d
        print("Keliling lingkaran adalah: " + str(keliling))
    else:
        print("Input selain angka, desimal terdeteksi. mengehentikan python")
else:
    print("Input selain a/b. menhentikan python")
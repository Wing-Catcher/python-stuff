# project membuat kalkulator phytagoras

print("Selamat datang diprogram KALKULATOR PHYTAGORAS SEDERHANA")
print("*Hanya mendukung bilangan bulat, input desimal masih dalam pengembangan.")
print("Python to executable, https://github.com/brentvollebregt/auto-py-to-exe")
print(
    
)
# Mengidentifikasi apa yang akan dicari dari sebuah segitiga
print("Silahkan pilih komponen segitiga apa yang akan dicari")
print("(a) Sisi Horizontal/Vertikal")
print("(b) Sisi Miring/Hipoterusa")
print(

)
# mengeksekusi input
pilihan = input("Pilihan: ").lower() #menghindari case sensitive
print(

) 
if pilihan == "a":
    print("Silahkan masukkan komponen yang diketahui:")
    diket_miring = input("Panjang sisi miring: ")
    diket_tegak = input("Panjang salah satu sisi tegak: ")
    # jika input benar, input adalah angka
    if diket_miring.isdigit() and diket_tegak.isdigit():
        #konversi nilai ke integer
        diket_miring = int(diket_miring)
        diket_tegak = int(diket_tegak)
        # implementasi rumus
        miring_2 = (diket_miring)**2
        tegak_2 = (diket_tegak)**2
        hasil_tegak = (miring_2 - tegak_2)**0.5
        print(
            
        )
        input("Klik enter untuk menampilkan hasil")
        print("Salah satu sisi tegaknya adalah: " + str(hasil_tegak))
        print("Kalkulator Phytagoras Sederhana by: Raffy IX-B/19")
        input("Press enter to exit")
    else:
        print("Input selain angka terdeteksi. Menghentikan python.")
        print("Kalkulator Phytagoras Sederhana by: Raffy IX-B/19")
        input("Press enter to exit")
elif pilihan == "b":
    print("Silahkan masukkan komponen yang diketahui:")
    diket_tegak1 = input("Panjang sisi tegak pertama: ")
    diket_tegak2 = input("Panjang sisi tegak kedua: ")
    # jika input benar, input adalah angka
    if diket_tegak1.isdigit() and diket_tegak2.isdigit():
        #konversi nilai ke integer
        diket_tegak1 = int(diket_tegak1)
        diket_tegak2 = int(diket_tegak2)
        # implementasi rumus
        tegak1_2 = (diket_tegak1)**2
        tegak2_2 = (diket_tegak2)**2
        hasil_miring = (tegak1_2 + tegak2_2)**0.5
        print(

        )
        input("Klik enter untuk menampilkan hasil")
        print("Salah satu sisi tegaknya adalah: " + str(hasil_miring))
        print("Kalkulator Phytagoras Sederhana by: Raffy IX-B/19")
        input("Press enter to exit")
    else:
        print("Input selain angka terdeteksi. Menghentikan python.")
        print("Kalkulator Phytagoras Sederhana by: Raffy IX-B/19")
        input("Press enter to exit")
else:
    print("Input selain a/b terdeteksi. Menghentikan python.")
    print("Kalkulator Phytagoras Sederhana by: Raffy IX-B/19")
    input("Press enter to exit")
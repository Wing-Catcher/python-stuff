"""
variabel adalah object yang didefinisikan sebagai wadah untuk nilai didalamnya
str/string = "abc"
int/integer = 123
float = 12.223
"""

# nilai tipe str/string
nama_depan = "ahmad"
nama_belakang = "fauzan"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_depan) #menampilkan isi dari variabel
print("halo, " + nama_lengkap) # kombinasi nilai print dan nama_lengkap
print(type(nama_lengkap)) # menampilkan jenis nilai yang dieksekusikan >> string
print()

# nilai tipe int/integer
umur = 16
umur = umur + 1
print(umur)
umur += 1
print(umur)
print(type(umur))
print()
# dibawah ini adalah typecasting
# print str dengan int datatype
"""
menampilkan nilai yang berbeda jenis harus menggunakan type casting
nilai angka bisa dicast menjadi integer/float
namun nilai karakter(abc) tidak bisa dicat float atau integer, hanya string
kesimpulan: ubah semua menjadi string jika terdapat angka dan huruf
"""
print(nama_lengkap +" Ananda berumur: "+ str(umur) + " tahun.") # jenis_data(variabel) >> str(umur)
print()

# nilai tipe float
tinggi = 230.2
print(tinggi)
print(type(tinggi))

# print str dengan float datatype
print ("Tinggi anda adalah: " + str(tinggi) + " cm.")
print()

# nilai tipe boolean (true/false)
human = False
print(type(human))
print(human)

#print str dengan boolean
print("Apakah anda seorang human?: " + str(human))
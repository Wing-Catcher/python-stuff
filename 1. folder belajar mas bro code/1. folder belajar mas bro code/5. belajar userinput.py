# bagaimana cara menerima input dari user (terminal)
"""
input adalah perintah yang meminta user untuk memasukkan 
nilai entah itu menggunakan variabel maupun tidak
"""
#tanpa diberi variabel
input("Siapakah nama anda? ")
print()

#diberi variabel
nama = input("Siapakah nama anda?: ")
print("Halo " + nama)
print()

#form berbeda
umur1 = input("Masukkan tanggal sekarang: ")
umur2 = input("MAsukkan tanggal lahir anda: ")
umur1, umur2 = int(umur1), int(umur2)
#typecasting
print("Umur anda sekarang adalah: " + str(umur1 - umur2)) # cast ke bentuk string
print()

"""
nilai input yang akan dimasukkan user dapat dicasting melalui baris input itu juga
seperti contoh dibawah ini
"""
#alternatif
bilangan = int(input("berapa?"))
print(type(bilangan))

#alternatid float
bilangan1 = float(input("Bilangan desimal / bulat:"))
print(type(bilangan1))

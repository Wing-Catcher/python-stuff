#mengimpor math
"""
import math adalah perintah untuk mengimpor modul matematika kompleks dari perpustakaan python
math ini memberi kebebasan lebih dalam mengoperasikan matematika pada nilai
"""
import math

pi = 3.14
a = 123
b = 225
c = 885

#bulatan umum
"""
membulatkan umum, 1 sampai 4 akan dibulatkan bawah/tetap sebelum koma.
5 sampai enam akan dibulatkan keatas/menambahkan +1 diangka sebelum koma
"""
print(round(pi))

#pembulatan dengan math
print(math.ceil(pi)) #membulatkan ke atas
print(math.floor(pi)) #membukatkan ke bawah

#nilai absolut
"""
Nilai absolut dari suatu angka adalah nilai numerik dari angka tersebut tanpa
memperhitungkan tanda positif atau negatifnya. Ini adalah jarak dari angka tersebut
ke titik nol pada garis bilangan. Misalnya, nilai absolut dari -5 adalah 5
dan nilai absolut dari 5 juga adalah 5. Dalam notasi matematika,
nilai absolut (|x|) dari suatu bilangan (x) dapat dinyatakan sebagai x jika x positif atau sama dengan
nol, dan -x jika x negatif.
"""
print(abs(pi))

#perpangkatan / power
"""
Variabel a dinyatakan sebagai bilangan basis dan 2 dinyatakan sebagai eksponen
"""
print(pow(a,2)) 
print(math.pow(a,2)) # menggunakan modul matematika (math.pow(x,n))

# akar square root
"""
mencari bilangan akar dengan m odul matematika
(math.sqrt(n))
"""
print(math.sqrt(420))

"""
mencari nilai terbesar / terkecil dari beberapa variabel atau nilai
atau bisa dianalogikan sebagai sortir
"""
# nilai terbesar/maks
print(max(a,b,c))
# nilai terendah min
print(min(a.b.c))

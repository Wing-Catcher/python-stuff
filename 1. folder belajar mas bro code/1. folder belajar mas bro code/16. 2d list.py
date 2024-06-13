"""
sebuah list dari list
multidimensional list
"""
minuman = ["jeruk", "kopi", "teh"]
makan_malam = ["pizza", "hamburger", "hotdog"]
makanan_penutup = ["cake", "es krim"]

semua = [minuman, makan_malam, makanan_penutup]
print(semua)

#Pengecualian dengan urutan[n]
try: # kemungkinan berhasil / exit code 0
    print(semua[0]) # menampilkan list dari n [0]"minuman"
    print(semua[4][1]) # menampilkan list "minuman" dan hanya mengambil urutan [1] sebagai output ("Kopi")
except IndexError: # pengecualian ketika ditemukan indexerror
    print("Diluar jangkauan")
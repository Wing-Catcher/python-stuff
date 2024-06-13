"""
daftar / list
digunakan untuk menaruh item banyak didalam satu variabel
"""

makanan = ["pizza", "hotdog", "Soto babat", "Pudding"]
print(makanan[0]) # kurung kotak mendefinisikan n urutan
print(makanan[1])

makanan[0]= "Indomie"
print(makanan[0]) # urutan pertama list didefinisikan sebagai 0

for x in makanan:
    print(x) # x = semua
    
"""
fungsi fungsi list
"""

makanan.append("Ice cream") # Menambhakan "ice cream" pada urutan setealh yang terakhir
makanan.remove("Soto babat") #Menghapus item didalam list yang bernilai "Soto babat"
makanan.pop() #Menghapus is list paling terakhir
makanan.insert(0,"cake") # pada urutan n diganti dengan "cake"
makanan.sort() # alphabetical
makanan.clear #mewmbersihkan semua
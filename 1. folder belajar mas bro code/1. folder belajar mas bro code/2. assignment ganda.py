# multiple assignment / assignment ganda = mengizinkan kita memasukkan beberapa variabel dalam satu baris saja

# Contoh tanpa penerapan
print("Contoh tanpa penerapan:")
nama = "Wing"
umur = 21
attractive = False
print(nama)
print(umur)
print(attractive)
print()
"""
melakukan multiple assignment harus dilakukan secara urut dan teliti dalam menentukan koma dan
jenis data yang digunakan
"""
# Contoh penerapan persis dengan contoh 1
print("Contoh dengan penerapan multiple assignment:")
nama2, umur2, attractive2 = "Catcher", 21, True
print()

# Contoh penerapan dengan nilai sama untuk variabel banyak
# Dafa = 30
# Dani = 30
# Zalfa = 30
Dafa = Dani = Zalfa = 30 
"""
a, b, c = 10
python akan mendefiniskan nilai dari a b dan c adalah nilai setelah "c"
yaitu 30 (integer)
"""
print(Dafa)
print(Dani)
print(Zalfa)
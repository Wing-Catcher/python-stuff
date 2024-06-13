# pernyataan id = sebuah blok kode yang akn dieksekusi jika kondisi = "true"
print("Contoh:")

age = int(input("berapa umur anda: "))
print()

if age == 100: #comparator sama
    print("You are century old")
elif age >= 18: #-> jika utama
    print("You are an adult.")
elif age < 0: #-> jika alternate
    print("You havent born yet")
else: #-> tidak memenuhi semua diatas
    print("You are a child")
# slicing = membuat substring dengan mengekstrak elemen dari string lain
#           indexing[] or slice()
#           [start:stop:step]
hint = "remember inclusive and exclusive"

print("contoh")
nama = "Yanto Well"

nama_depan = nama[0:5]
nama_belakang = nama[6:10]
funky_name = nama[0:10:2]
reversed_nama = nama[::-1]

print(nama_depan)
print(nama_belakang)
print(funky_name)
print(reversed_nama)

print("contoh web")
web = "http://abc.com"
web2 = "http://wikipedia.com"

sliced = slice(7,-4) #-> ibaratkan gunting
print(hint)

print(web[sliced])
print(web2[sliced])

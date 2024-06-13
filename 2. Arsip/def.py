# ngerteni daf def daf def:))

def hitung_luas_lingkaran(jari_jari):
    pi = 3.14
    luas = pi * (jari_jari ** 2)
    return luas

# Memanggil fungsi hitung_luas_lingkaran
con1 = input("lanjut? y/n: ")
if con1 == "y":
    r = 5
    luas = hitung_luas_lingkaran(r)
    print("Luas lingkaran dengan jari-jari", r, "adalah:", luas)
elif con1 == "n":
    print("Cancelled")
else:
    print("cancelled")

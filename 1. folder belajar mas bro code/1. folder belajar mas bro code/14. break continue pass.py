"""
Loop control statements
= Mengubah sebuah elselusi loop dari urutan normalnya
# break =  digunakan untuk menghentikan semua loop (yang berjalan)
# continue = melewati ke iterasi selanjutnya dari loop
# pass = tidak melakukan apa pun, bertindak seperti placeholder.
"""

while True:
    name = input("Your name: ")
    if name != "":
        break # ! menandakan false

phone_num = "123-123-123"
for i in phone_num:
    if i == "-":
        continue
    print(i, end="") # end dari print default adalah enter, dengan end = "" maka end hanya sebuah baris kosong
    
for i in range(1,21): #menghitung range dari 1 sampai 21 (20)
    if i == 13:
        pass # melewati nilai "13"
    else:
        print(i) # menampilkan hasil i setelah di "pass"
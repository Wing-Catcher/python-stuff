# mengetahui apakah berisi koma dan dianggap sebagai bilangan desimal
print("")
angka = input("Masukkan input anda: ")
if "." or "," in angka:
    angka.replace(",", ".")
    angka = float(angka)
    print("Angka merupakan float" + str(angka))
elif angka.isalpha():
    print("Angka yang anda masukkan berisi huruf")
elif angka.isdigit():
    print("HAnya berisi")
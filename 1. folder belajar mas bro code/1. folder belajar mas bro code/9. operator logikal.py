#Logical operator: digunakan untuk cek apakah dua atau lebih pernyataan kondisionala adalah "true"

suhu = int(input("Berapa suhu luar ruangan: "))

if suhu >=0 and suhu<= 30:
    print("Suhu luar ruangan stabil.")
elif not(suhu <= 1000): #false to true true to false
    print("bruh")
elif suhu <0 or suhu >30:
    print("suhu luar ruanagn tidak stabil.")
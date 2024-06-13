# forloop adalah keadaan yang akan dijalankan kode blocknya untuk waktu yang terbatas
#   while loop = unlimited
# for loop = limited
print("Contoh")
for i in range(10):
    print(i+1)
print()
a = range(10)
print(a)
print()

for i in range(50,100+1): #50 start point(inklusif) 100 indexing(eksklusif)
    print(i)
for i in range(50,100+1,2): #50 start point(inklusif) 100 indexing(eksklusif) 2 langkahan
    print(i)
for i in "Halo Mas Bro":
    print(i)

import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year")
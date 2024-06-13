"""
Nested loop = the "The inner loop" will finish all of it's iterations before
finishing one iteration of the outer loop

Nested loop = "Loop dalam" akan menyelesaikan semua iterasi sebelumnya
menyelesaikan satu iterasi dari loop luar
"""
print('Menggambar persegi')

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
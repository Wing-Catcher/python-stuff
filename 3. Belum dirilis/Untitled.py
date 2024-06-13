"""
print("hello world")
print()
digit1 = float(input("Insert your number: "))
print(digit1)
"""
print("Test input desimal")
print("=========")
print()
num1 = input("Insert 1st number: ")
num2 = input("Insert 2st number: ")
print(num1, num2)
print("=== Konversi ===")
if "." in num1 or num1.isdigit() and "." in num2 or num2.isdigit():
    try:
        num1, num2 = float(num1), float(num2)
        print("true")
        print(num1 + num2)
    except ValueError:
        print("404 x_x")
else:
    print("false")
print("hello world")
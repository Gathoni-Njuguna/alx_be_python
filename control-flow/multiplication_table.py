number = int(input("Enter a number to see its multiplication table:"))
print(f"Multiplication table for {number}:")
for i in range(1,11):
    print(number ," * " ,i ," = " ,number * i)
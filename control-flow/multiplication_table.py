# Prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
print(f"Multiplication table for {number}:")
for y in range(1, 11):
    product = number * y
    print(f"{number} * {y} = {product}")
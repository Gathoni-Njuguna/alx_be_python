size = int(input(" Enter the size of the pattern:"))
row = 0
print("Enter the size of the pattern:", size)
while row < size:
    for col in range(size):
        print("*", end="")
    # Move to the next line after completing a row
    print()
    # Increment row counter
    row += 1
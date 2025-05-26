pattern = int(input(" Enter the size of the pattern:"))
row = 0
print("Enter the size of the pattern:", pattern)
while row < pattern:
    for col in range(pattern):
        print("*", end="")
    # Move to the next line after completing a row
    print()
    # Increment row counter
    row += 1
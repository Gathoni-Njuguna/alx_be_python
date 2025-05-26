# pattern_drawing.py
# Draws a square pattern of asterisks based on user input

# Prompt user for pattern size with exact required string
size = int(input("Enter the size of the pattern:"))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns
    for col in range(size):
        print("*", end="")
    # Move to the next line after completing a row
    print()
    # Increment row counter
    row += 1
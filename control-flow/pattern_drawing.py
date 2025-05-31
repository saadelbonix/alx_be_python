# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for each row
while row < size:
    # Use a for loop for each column (asterisks in the row)
    for col in range(size):
        print("*", end="")  # Print without newline
    print()  # Move to the next line after each row
    row += 1

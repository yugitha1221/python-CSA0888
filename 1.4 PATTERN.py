# Get user input
start_number = float(input("Enter the starting number: "))
max_lines = int(input("Max number of lines to be printed: "))

# Initialize the current number
current_number = start_number

# Loop to print the pattern
for i in range(1, max_lines + 1):
    for j in range(i):
        print(" ", end=" ")
        current_number += 0.1
    print()  # Move to the next line

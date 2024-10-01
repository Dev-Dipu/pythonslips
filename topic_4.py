# Example: Create a list of numbers and check for even or odd

# Step 1: Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 2: Loop through the list and check if each number is even or odd
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

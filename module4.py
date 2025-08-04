# Ask for the number of values
N = int(input("Enter a positive integer N: "))

# Read N numbers one by one and store them in a list
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Ask for the value to search
X = int(input("Enter a number X to search for: "))

# Check if X is in the list and print the 1-based index or -1
if X in numbers:
    index = numbers.index(X) + 1  # Convert to 1-based index
    print(index)
else:
    print(-1)

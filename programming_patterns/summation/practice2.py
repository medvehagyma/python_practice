# We have a bunch of single digit positive intigers. Let's calculate the sum of their squares.

# inputs
N = int(input("Enter the number of numbers.\n"))
numbers = []

for i in range (0, N) :
    numbers.append(int(input("Enter the list's numbers.\n")))


# algorithm
totalSum = 0

for i in range (0, len(numbers)) :
    totalSum += numbers[i]**2

# outputs
print(totalSum)

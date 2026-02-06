# We have 5 integers in a list. Let's calculate the sum of their cubes.

# inputs

numbers = []

for i in range (0, 5) :
    numbers.append(int(input("Enter the list's numbers.\n")))


# algorithm
totalSum = 0

for i in range (0, len(numbers)) :
    totalSum += numbers[i]**3

# outputs
print(totalSum)
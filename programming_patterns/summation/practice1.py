# We have a bunch of positive integers in a list. Let's calculate their total sum.

# inputs
numbers = [23, 4, 0, 2, 11, 52, 77, 15]

# algorithm
totalSum = 0

for i in range (0, len(numbers)) :
    totalSum += numbers[i]

# outputs
print(totalSum)

    

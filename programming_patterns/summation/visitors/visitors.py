# In a list we have the number of visitors to a shop for each day of one week (7 days). 
# This means the number of elements in the list is of fixed size 7. 
# Calculate the total number of visitors to the shop for the entire week!

# inputs

visitors = [37, 17, 24, 26, 51, 62, 21]

# algorithm

def calcVisitors (visitors) :
    totalSum = 0

    for i in range (0, len(visitors)) :
        totalSum += visitors[i]
    
    return totalSum


# output

print(calcVisitors(visitors))

# In a list we have the amounts of minutes a University student has been late to class. 
# Their attendance is invalid and counts as a missed class if they have been late for more than 15 minutes. 
# Count the number of times the student missed their class and their attendance was not recorded!


# inputs

minutes = [4, 6, 0, 13, 16, 0, 3, 0, 8, 17]


# algorithm

def countMin (minutes) :

    cnt = 0

    for i in range (0, len(minutes)) :
        if minutes[i] > 15 :
            cnt += 1

    return cnt


# outputs

print(countMin(minutes))
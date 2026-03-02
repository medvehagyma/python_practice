# We have the laptimes of a track runner. Calculate the average time.

import sys


# inputs

# lapTimes = [37.2, 36.6]

lapTimes = [35, 36]

for lap in lapTimes :
    if lap <= 0 : sys.exit(1)


# algorithm

avg = 0

for i in range (0, len(lapTimes)) :
    avg += lapTimes [i]/len(lapTimes)


# outputs

print(avg)

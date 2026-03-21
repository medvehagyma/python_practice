# We measured the outside temperatures for some days. Count how many days the temperature was above 28 °C.

# inputs

n = 6
temps = [23, 26.3, 29, 36, 37.6, 39]


# algorithm

def cntHotterThan28 (temps) :

    cnt = 0

    for i in range (0, len(temps)) :
        if temps[i] > 28 :
            cnt += 1

    return cnt

# outputs

print(cntHotterThan28(temps))

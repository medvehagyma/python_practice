# írd ki a listából a legnagyobb számot
# írd ki a második legnagyobb számot
# írd ki a legkisebb számot
# írd ki az összes páros számot
# írd ki az összes páratlan számot
# írd ki a páros számok számát
# írd ki a negatív számokat
# írd ki a negatív számok számát

numbers = [-44, -12, -5, 0, 4, 29, 35, 60, 85, 111]

# kiírom a legnagyobb számot

def maxNum (number) :
    maxNumber = number[0]

    for num in number :
        if num > maxNumber :
            maxNumber = num
    return maxNumber

print("A legnagyobb szám:", maxNum(numbers))


# kiírom a második legnagyobb számot

def secondMax (number) :
    maxNumber1 = maxNum(number)
    maxNumber2 = number[0]

    for num in number :
        if num != maxNumber1 and num > maxNumber2 :
            maxNumber2 = num
    return maxNumber2

print("A második legnagyobb szám:", secondMax(numbers))


# kiírom a legkisebb számot

def minNum (number) :
    minNumber = number[0]

    for num in number :
        if num < minNumber :
            minNumber = num
    return minNumber

print("A legkisebb szám:", minNum(numbers))


# kiírom az összes páros számot

def isEven (number) :
    isEven = number % 2 == 0
    return isEven

for num in numbers :
    if isEven(num) : print("Páros szám a(z):", num)


# kiírom az összes páratlan számot

for num in numbers :
    if not isEven(num) : print("Páratlan szám a(z):", num)


# kiírom a páros számok számát
def countEven (number) :
    count = 0

    for num in number :
        if isEven(num) : count += 1
    return count

print("A páros számok száma:", countEven(numbers))

# kiírom a negatív számokat
def isNegative (number) :
    isNegative = number < 0
    return isNegative

for num in numbers :
    if isNegative(num) : print("Negatív szám a(z):", num)

# kiírom a negatív számok számát
def countNegative (number) :
    count = 0

    for num in number :
        if isNegative(num) : count += 1
    return count

print("A negatív számok száma:", countNegative(numbers))
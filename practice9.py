# Egy listában tároljuk az elmúlt n nap maximálisan mért hőmérsékleteit
# Add meg, hogy mi volt a legmagasabb mért hőmérséklet az elmúlt n napban!
# Példa bemenet: [28, 25, 26, 31, 29, 30, 28]
# Példa kimenet: 31



temperatures = [28, 25, 26, 31, 29, 30, 28]
temperatures2 = [30, 35, 28]



# itt is a globális scope van

def maxTemp (myParameter):
    # itt van a maxTemp függvéby scope-ja
    '''
    fogom az első elemet a tömbből, és elrakom egy maximum vagy maxTemperature vagy retVal változóba
    mert ez az amit eddig a legnagyobbnak találtam

    elemenként megnézem a myParameter listát és ha éppen egy olyan elemet találok, ami nagyobb az eddigi legnagyobbnál
    akkor az eddigi legnagyobbat felülírom az újonnan találttal
    '''
    maxTemperature = myParameter[0]
    
    for measurement in myParameter :
        if measurement > maxTemperature :
            maxTemperature = measurement
    return maxTemperature


# itt kint a globális scope van
print(maxTemp(temperatures))
print(maxTemp(temperatures2))


def minTemp (measurements):
    minTemperature = measurements[0]

    for measurement in measurements :
        if measurement < minTemperature :
            minTemperature = measurement
    return minTemperature


print(minTemp(temperatures))
print(minTemp(temperatures2))
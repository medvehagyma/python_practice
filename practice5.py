
# TODO: Implementálj egy canBeDividedBy5 nevű függvényt, ami egy logikai értéket ad vissza arról
# hogy a paraméterként kapott szám osztható-e 5-el!

def canBeDividedBy5 (number):
    retVal = number%5==0
    return retVal

if canBeDividedBy5(int(input("Irj be egy szamot: "))):
    print("Oh ez a szám osztható 5-el")
else:
    print(":( nem osztható 5-el")
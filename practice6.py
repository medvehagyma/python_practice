# TODO: Irj egy greeting nevű függvényt, ami paraméterként vár egy stringet és eléfűzi, hogy "Szia "!

def greeting (name):
    retVal = ('Szia '+name+'!')
    return retVal
print(greeting("Encsi"))
print(greeting("Falesz"))
print(greeting(input()))
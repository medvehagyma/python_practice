# f(x) := x^2 + 1 -- függvény definíció
# f(5) = 5^2 + 1 = 26
# f(x) = 37 -- számítsd ki az x-et!
# x^2 + 1 = 37 -> x^2 = 36 -> x1 = 6, x2 = -6

# függvény definíciója: azt mondja meg, hogy MIT kell csinálni
# függvény paramétere: azt mondja meg, hogy MIVEL kell azt csinálni

def greeting(name): # függvénydefiníció
    return "Hello, " + name

print(greeting("Encsi")) # függvényhívás -> arra értékelődik ki, hogy "Hello, Encsi"
print(greeting("Falesz")) # arra értékelődik ki, hogy "Hello, Falesz"

def add(num1, num2):
    return num1 + num2

print(add(3, 2)) # arra értékelődik, ki hogy: 5
# def add(3, 2):
#    return 3 + 2
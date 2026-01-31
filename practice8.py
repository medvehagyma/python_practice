# Ha van több adat, amik ugyanolyan típusúak, de mást jelölnek, azokat listába lehet rakni.

numbers = [1, 2, 3, 4]
fruits = ['apple', 'kiwi', 'banana']

print(numbers [0])
print(fruits [0])
print(fruits [1])

fruits.append('cherry')
print(fruits [3])

for fruit in fruits:
    print('I just found a(n) '+fruit+'.')
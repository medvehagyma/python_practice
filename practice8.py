# Ha van több adat, amik ugyanolyan típusúak, de mást jelölnek, azokat listába lehet rakni.

# This is a list. In most other programming languages, we call similar data structures an array.
# It contains several pieces of distinct, but logically connected data.
numbers = [1, 2, 3, 4]
fruits = ['apple', 'kiwi', 'banana']

print(numbers [0]) # We can take elements of lists by providing the indexes of the elements. We start indexing from 0.
print(fruits [0])
print(fruits [1])

fruits.append('cherry') # Lists have built-in functions like append. This will place the given value at the end of the list.
print(fruits [3])

for fruit in fruits: # For loops can be used to perform some action on each element of a list. Here fruit will assume the value of each element in the fruits list.
    print('I just found a(n) '+fruit+'.')
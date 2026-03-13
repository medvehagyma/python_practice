print('Hello World!') # The print function will display a given text on the screen.
# This is a variable. It is called num and it is assigned a value of 7. Now num will hold this value until it is changed and can be used for calculations.
num=7
print(num) # This will display 7 on the screen; always the value contained within the variable.
# We can reassign the value contained within num. Python programs are read from top to bottom. Previously num was 7, now it will be 1 until it is changed again.
num=1
print(num) # This will now display 1.
floatingPointNum=2.71 # Variables can hold many different types of values. This is a floating point number.
print(floatingPointNum)

# In programming we often work with mathematical logic. We work with statements that have either a true value or false value. These can also be stored in variables.
logic1=True
logic2=False
logic3=5>3 # True
logic4=4>9 # False
logic5=floatingPointNum>3 # We take the current value of floatingPointNum and compare it to 3. This essentially makes this expression: 2.71 > 3 (False)

# Many times we want to do different things based on some condition. If the condition is true, we do one thing and if it's false, we do another thing.
# This can be done with if-else structures.
if floatingPointNum>3:
    print('a floatingPointNum lehet Pi')
else :
    print('a floatingPointNum biztosan nem Pi')    

# If the condition is true, we execute the code in the "true"/if branch and do NOT execute the code in the "false"/else branch.
floatingPointNum=3.14
if floatingPointNum>3:
    print('a floatingPointNum lehet Pi')
else :
    print('a floatingPointNum biztosan nem Pi')


# If we want to do something over and over again, it would be cumbersome to type the code out 2, 3, 5, 10, 3 million times.
# Instead we use loops.
# A while loop is given a condition and will execute the code within itself again and again as long as the condition is true.
# In Hungarian we may call this "feltételes ciklus".

#a num értéke 1
#növeljük meg a num értékét egyesével, addig, amíg 10 nem lesz. minden növelésnél írjuk ki

# num is still 1, from the beginning of this file. So to evaluate the condition, we substitute it's value in there: 1 < 10. This is true, so we execute the code.
# Then after the first iteration of this loop num will be 2. We come back to condition to evaluate it again: 2 < 10. Still true, we execute the code again.
# We go again and again until num becomes 10. Now we evaluate the condition with this value: 10 < 10. This is false, so the condition breaks and the while loop ends.
# After the loop ends we go on with the rest of the program.
while num<10:
    #num=num+1 
    num+=1 # Short form of adding 1 to the value of a number.
    print('num értéke '+str (num)) # Since 'num értéke' is a string and num is a number, we have to convert num into a string for them to be concatenated.

# Another kind of loop is the for loop or iterative loop. We give it a range of values and in each iteration the iterator variable
# will assume the next value in the range. We can then use it inside the loop for whatever we want.
for i in range(0,10):
    print('i értéke '+str (i))

# If we want to do something over and over many times in different places in our codebase, we can define functions for them.
# These will be little self-contained programs in and of themselves. When we write their definitions with def, they will not immediately be executed.
# Instead Python will just remember that "Oh, to tell whether a number is even or not, we have to take it's remainder after dividing by 2 and see if it's 0 or not."
def isEven (number):
    even=number%2==0
    return even

# After defining a function we can call it. If it has parameters, we can assign values to the parameters within the parentheses.
print(isEven(1)) # even=1%2==0 -> False
print(isEven(6)) # even=6%2==0 -> True

#The input function can be used to read a string from the keyboard. If we want to read a number from the keyboard, we have to convert it into an int too!
num2=int(input())
if isEven (num2):
    print('a num2 páros')
else :
    print('a num2 páratlan')
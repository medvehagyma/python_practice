print('Hello World!')
num=7
print(num)
num=1
print(num)
floatingPointNum=2.71
print(floatingPointNum)

logic1=True
logic2=False
logic3=5>3
logic4=4>9
logic5=floatingPointNum>3

if floatingPointNum>3:
    print('a floatingPointNum lehet Pi')
else :
    print('a floatingPointNum biztosan nem Pi')    

floatingPointNum=3.14
if floatingPointNum>3:
    print('a floatingPointNum lehet Pi')
else :
    print('a floatingPointNum biztosan nem Pi')


#a num értéke 1
#növeljük meg a num értékét egyesével, addig, amíg 10 nem lesz. minden növelésnél írjuk ki

while num<10:
    #num=num+1 
    num+=1
    print('num értéke '+str (num))

for i in range(0,10):
    print('i értéke '+str (i))


def isEven (number):
    even=number%2==0
    return even

print(isEven(1))
print(isEven(6))


num2=int(input())
if isEven (num2):
    print('a num2 páros')
else :
    print('a num2 páratlan')
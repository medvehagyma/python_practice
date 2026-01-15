import random

secretNum = random.randint(8,3333)
guess = int(input('Írj be egy számot 8 és 3333 között. '))

#meg akarjuk nézni, hogy a secretNum és a guess egyenlőek-e. Ha igen, akkor vége a programnak.
#Ha nem, akkor mégegyszer be kell kérni egy számot a guess változóba.
#Ezt addig kell csinálni, amíg a guess nem egyenlő a secretNummal.

while guess!=secretNum:
    if secretNum>guess:
        print('A gondolt szám nagyobb, mint amit tippeltél.')
    else :
        print('A gondolt szám kisebb, mint amit tippeltél.')
    guess = int(input('Írj be egy számot 8 és 3333 között. '))
print('Nagyon ügyes vagy!')
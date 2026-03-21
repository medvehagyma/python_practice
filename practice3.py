import random # Many useful things are contained within modules/packages. random is a package containing many functions dealing with randomness

# random.randint will generate a random number for you between the minimum and maximum bounds that you specify for it.
secretNum = random.randint(8,3333)
guess = int(input('Írj be egy számot 8 és 3333 között. '))

#meg akarjuk nézni, hogy a secretNum és a guess egyenlőek-e. Ha igen, akkor vége a programnak.
#Ha nem, akkor mégegyszer be kell kérni egy számot a guess változóba.
#Ezt addig kell csinálni, amíg a guess nem egyenlő a secretNummal.

while guess!=secretNum: # While the player's guess is not equal to the secret number we keep asking for new guesses.
    if secretNum>guess:
        print('A gondolt szám nagyobb, mint amit tippeltél.') # We tell the player that the guessed number is too little.
    else :
        print('A gondolt szám kisebb, mint amit tippeltél.') # We tell the player that the guessed number is too large.
    guess = int(input('Írj be egy számot 8 és 3333 között. ')) # We ask for a new guess with the input function and emplace it in guess

print('Nagyon ügyes vagy!') # If the loop ended, that means guess == secretNum, meaning the player guessed correctly, so it's time to congratulate them
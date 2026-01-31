import random
import math

playerGuesses=int(input('Szeretnél te tippelni? 1) én tippelek 2) a gép tippel\n'))
# ha a playerGuesses értéke 1, akkor a gép gondol egy számot és a játékos tippel, ha 2 akkor fordítva.


if playerGuesses == 1:
    secretNum = random.randint(8,3333)
    guess = int(input('Írj be egy számot 8 és 3333 között.\n'))

    counter = 1

    while guess!=secretNum:
        counter += 1
        if secretNum>guess:
            print('A gondolt szám nagyobb, mint amit tippeltél.')
        else :
            print('A gondolt szám kisebb, mint amit tippeltél.')
        guess = int(input('Írj be egy számot 8 és 3333 között. '))
    print('Nagyon ügyes vagy!')
    print(str(counter)+' lépés kellett hozzá')

else :
    secretNum=int(input('Gondolj egy számot 0 és 10000 között.\n'))
    minGuess=0
    maxGuess=10000

    counter=1

    guess=(maxGuess-minGuess)/2

    while secretNum!=guess:
        counter+=1
        if guess<secretNum:
            print('Most a '+str(guess)+' számot tippeltem, de ez túl kicsi.' )
            minGuess=guess
            guess=math.floor((maxGuess-minGuess)/2+minGuess)
            
        else :
            print('Most a '+str(guess)+' számot tippeltem, de ez túl nagy.' )
            maxGuess=guess
            guess=math.floor((maxGuess-minGuess)/2+minGuess)
        

    print('Nyertem! '+str(guess)+ ' a szám.')
    print(str(counter)+' lépés kellett hozzá')
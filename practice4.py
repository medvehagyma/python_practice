import math
# math.floor(2.71) ez lefelé kerekíti
# math.floor((maxGuess-minGuess)/2+minGuess)
# math.floor((maxGuess-minGuess)/2+minGuess)



secretNum=int(input('Gondolj egy számot 0 és 10000 között.'))
# én mint programozó ígérem, hogy nem fogom megnézni a kódban, hogy mi a secretNum értéke
# ------------------------------------------------------------------------------------------

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
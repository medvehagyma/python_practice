# Írj egy függvényt, ami egy egész számot vár paraméterül
# és eldönti róla, hogy nagyobb-e 10-nél! A visszatérési érték tehát logikai (boolean érték)
# A függvény segítségével döntsd el a számokról 0-tól 20-ig, a -50-ről és a 65-ről, hogy nagyobbak-e 10-nél:
# a kimenetre írj ki egy szöveget arról, hogy az éppen vizsgált számról milyen eredményt ad a függvényed

num=int(input('Kérlek, írj be egy számot.'))
if num>10:
    print('nagyobb, mint 10')
else :
    print('kisebb, mint 10')


def isGrThan10(num):
    greater=num>10
    return greater

print(isGrThan10(-50))
print(isGrThan10(65))
for i in range(0,21):
    if isGrThan10(i):
        print('a '+str(i)+' nagyobb, mint 10')
    else :
        if i==10: 
            print ('a '+str(i)+' éppen 10')
        else :
            print('a '+str(i)+' kisebb, mint 10')
      

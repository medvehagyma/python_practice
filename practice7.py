# TODO: Irj egy játékot, amiben a felhasználónak be kell írnia a billentyűzeten, hogy "left" vagy "right".
# A program először írja ki, hogy egy sötét barlang bejáratánál állsz és két út vezet befelé.
# Kérdezd meg a játékost, merre akar menni.
# Attól függően, hogy mit ír be futtasd le egy if-else valamelyik ágát!
# Az egyik ág (te döntöd el, melyik) vezessen egy kincshez, a másik ág egy sárkányhoz aki megeszi a játékost!
# Minden ilyen eseményt irj ki a képernyőre


whereToGo = input('Egy sötét barlang bejáratánál állsz és két út vezet befelé. Merre akarsz menni? (right, left) ')

# AMÍG a játékos jó szöveget nem ír be, addig szeretnénk újra kérni tőle a bemenetet
while whereToGo != 'right' and whereToGo != 'left':
    whereToGo = input('Rossz szót írtál be. írd be, hogy right vagy left. ')

if whereToGo == 'right':
    print('OMG! Megevett a sárkány!')
else :
    print('Megtaláltad a kincset.')
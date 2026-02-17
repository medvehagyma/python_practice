# Adott egy PTI-s hallgató jegyeinek listája különböző tantárgyakból. 
# Számoljuk meg, hogy hány tantárgyból lett legalább 4-es.


# inputs

grades = [2, 4, 5, 3, 4, 4, 3, 4]


# algorithm

def countGrades (grades) :

    cnt = 0

    for i in range (0, len(grades)) :
        if grades[i] >= 4 :
            cnt += 1
    
    return cnt


# outputs

print(countGrades(grades))
import random as rd
import matplotlib.pyplot as plot
def sim(n):
    deux = 0
    trois = 0
    quatre = 0
    cinq = 0
    six = 0
    sept= 0
    huit = 0
    neuf = 0
    dix = 0
    onze = 0
    douze = 0
    for i in range(n):
        x = rd.randint(1,6)
        y = rd.randint(1,6)
        if x+y == 2:
            deux += 1
        if x+y == 3:
            trois += 1
        if x+y == 4:
            quatre += 1
        if x+y == 5:
            cinq += 1
        if x+y == 6:
            six += 1
        if x+y == 7:
            sept += 1
        if x+y == 8:
            huit += 1
        if x+y == 9:
            neuf += 1
        if x+y == 10:
            dix += 1
        if x+y == 11:
            onze += 1
        if x+y == 12:
            douze += 1
    liste = []
    for i in deux, trois, quatre, cinq, six, sept, huit, neuf, dix, onze, douze:
        liste.append(i)
    print(liste)
    plot.bar([i for i in range(2,13)],liste)
    return plot.show()
n = int(input("Combien de fois voulez vous lancer les dés?\n"))
sim(n)
        
        

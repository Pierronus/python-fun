import random as rd
import matplotlib.pyplot as plot
def sim(n):
    un = 0
    deux = 0
    trois = 0
    quatre = 0
    cinq = 0
    six = 0
    for i in range(n):
        x = rd.randint(1,6)
        if x == 1:
            un += 1
        if x == 2:
            deux += 1
        if x == 3:
            trois += 1
        if x == 4:
            quatre += 1
        if x == 5:
            cinq += 1
        if x == 6:
            six += 1
    liste = []
    for i in un, deux, trois, quatre, cinq, six:
        liste.append(i)
    print(liste)
    plot.bar([i for i in range(1,7)],liste)
    return plot.show()
n = int(input("Combien de fois voulez vous lancer le dé?\n"))
sim(n)
        
        
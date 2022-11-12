import random as rd
import matplotlib.pyplot as plot

#avec x le nombre de dés à lancer et n le nombre de fois
def sim(x,n):
    liste = [0 for i in range(0,(6*x)+1)]
    for i in range(n):
        nbtot = 0
        for j in range(x):
            nb = rd.randint(1,6)
            nbtot += nb   
        liste[nbtot] = int(liste[nbtot]) + 1
    plot.bar([i for i in range(0,(6*x)+1)],liste)
    return plot.show()
        

n = int(input("Combien de fois voulez vous lancer les dés?\n"))
x = int(input("Combien de dés voulez vous lancer à chaque fois?\n"))
sim(x,n)        
        
        
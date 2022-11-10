from math import *

print("Avec a et b les 2 côtés adjacents de l'angle droit et h l'hypothénuse du triangle rectangle\n")

reply = input("Quel côté voulez vous calculer ? (a/b/h)\n")
if reply == "a":
    b = float(input("\nEntrez la valeur du côté b : "))
    h = float(input("Entrez la valeur du côté h : "))
    rep = sqrt(h**2 - b**2)
    print("On prend la racine carrée de l'expression h² - b² ce qui nous donne " + str(rep))    
elif reply == "b":
    a = float(input("\nEntrez la valeur du côté a : "))
    h = float(input("Entrez la valeur du côté h : "))
    rep = sqrt(h**2 - a**2)
    print("On prend la racine carrée de l'expression h² - a² ce qui nous donne " + str(rep)) 
elif reply == "h":
    a = float(input("\nEntrez la valeur du côté a : "))
    b = float(input("Entrez la valeur du côté b : "))
    rep = sqrt(a**2 + b**2)
    print("On prend la racine carrée de l'expression a² + b² ce qui nous donne " + str(rep))
else:
    print("Votre réponse n'est pas bonne : vous devez choisir entre a, b ou h")
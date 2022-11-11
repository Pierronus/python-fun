import random as rd
def pfc(choix):
    liste = ["pierre","feuille","ciseaux"]
    assert choix in liste, "Le choix doit etre soit pierre, soit feuille ou soit ciseaux"
    ordi = rd.choice(liste)
    if choix == "pierre":
            if ordi == "pierre":
                return "L'ordi a choisi la pierre, il y a match nul"
            if ordi == "feuille":
                return "L'ordi a choisi la feuille, il gagne"
            else:
                return "L'ordi a choisi les ciseaux, vous gagnez"
    if choix == "feuille":
            if ordi == "pierre":
                return "L'ordi a choisi la pierre, vous gagnez"
            if ordi == "feuille":
                return "L'ordi a choisi la feuille, il y a match nul"
            else:
                return "L'ordi a choisi les ciseaux, l'ordi gagne"
    if choix == "ciseaux":
            if ordi == "pierre":
                return "L'ordi a choisi la pierre, il gagne"
            if ordi == "feuille":
                return "L'ordi a choisi la feuille, vous gagnez"
            else:
                return "L'ordi a choisi les ciseaux, il y a match nul"
choix = input("Veuillez choisir entre pierre, feuille et ciseaux\n")
print(pfc(choix))
            
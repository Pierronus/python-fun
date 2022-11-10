def luhn(cb):
    assert len(cb) == 16, "Le numero de la CB doit être égal à 16"
    liste = [int(i) for i in cb]
    somme = 0
    
    
    for i in range(len(liste)-1):
        if i%2 == 1:
            somme = somme + liste[i]
        else:
            if int(liste[i])*2 > 9:
                somme = somme + (liste[i]*2) -9
            else:
                somme = somme + (liste[i]*2)
    p = 0
    for i in range(0,10):
        if (somme + i)%10 == 0:
            p = i
    if p == liste[15]:
        return True
    return False

num = input("Entrez le numéro de CB\n")

if luhn(num):
    print("Le numéro de CB est valide")
else:
    print("Le numéro de CB est invalide")
    
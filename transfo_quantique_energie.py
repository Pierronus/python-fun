def transfo(Ei, Ef):
    dE = Ef - Ei
    varjoule = abs(dE) * 1.6 * 10**-19
    lambd = (((6.63*10**-34)*3.0*10**8)/varjoule)*10**9
    return "La longueur d'onde est de " + str(lambd) + " nm"

etat_initial = float(input("Entrez la valeur numérique de l'etat initial\n"))
etat_final = float(input("Entrez la valeur numérique de l'etat final\n"))
print(transfo(etat_initial,etat_final))
    
    
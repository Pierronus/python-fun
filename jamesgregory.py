def james(n):
    nb = 0
    for i in range(0,n):
        nb += (((-1)**i )/ (2*i+1))
    nb = nb*4
    return nb
n = int(input("Entrez le nombre n : plus n se rapproche d'infini, plus pi est précis.\n"))

print(james(n))

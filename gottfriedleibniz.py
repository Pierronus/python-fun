def gottfried(n):
    nb = 0
    r = 0
    for i in range(1,n):
        if i%2 != 0:
            r = r+1
            if r%2 != 0:
                nb += (1/(i*(i+2)))
    nb = nb*8
    return nb
n = int(input("Entrez le nombre n : plus n se rapproche d'infini, plus pi est précis.\n"))

print(gottfried(n))

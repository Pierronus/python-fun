def john(n):
    nb = 1
    for i in range(1,n):
        nb = nb * (4*(i**2)) / (4*(i**2) - 1)
    nb = nb*2
    return nb

n = int(input("Entrez le nombre n : plus n se rapproche d'infini, plus pi est grand.\n"))

print(john(n))
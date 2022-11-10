def euler(n):
    nb = 1
    for i in range(3,n,2):
        denominateur = 1
        numerateur = 1
        t = 0
        for j in range(3, i+1):
            if j%2 != 0:
                denominateur = denominateur * j
                t = t+1
        for k in range(1,t+1):
            numerateur = numerateur * k
    
        nb = nb+ (numerateur/denominateur)
    nb = nb*2
    return nb
n = int(input("Entrez le nombre n : plus n se rapproche d'infini, plus pi est grand.\n"))

print(euler(n))
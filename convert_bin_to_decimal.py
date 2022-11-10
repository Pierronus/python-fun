def bintodec(entry):
    entry = str(entry)[::-1]
    nb = 0
    for i in range(len(entry)):
        if entry[i] == "1":
            nb = nb+(2**i)
    return nb
bina = input("Entrez un nombre binaire\n")
print(bintodec(bina))
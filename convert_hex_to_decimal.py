def hextodec(entry):
    entry = entry[::-1]
    table = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15,
        'a':10,
        'b':11,
        'c':12,
        'd':13,
        'e':14,
        'f':15,
        }
    
    nb = 0
    for i in range(len(entry)):
        nb = nb+ int(table[entry[i]]) * 16**i
    return nb

hexa = input("Entrez un nombre hexadécimal\n")
print(hextodec(hexa))
import random as rd
def passgen(n):
    symbols = ["%",".","*","$","#","&","@","!","?"]
    # min : chr 97 to 122
    # maj : chr 65 to 90
    pwd = ""
    for i in range(n):
        case = rd.randint(1,3)
        if case == 1:
            symbol = rd.randint(0,8)
            pwd += symbols[symbol]
        elif case == 2:
            char = rd.randint(97,123)
            pwd += str(chr(char))
        else:
            char = rd.randint(65,91)
            pwd += str(chr(char))
    return pwd
n = int(input("Quelle est la longueur du mot de passe désiré ?\n"))
print(passgen(n))
            
            
        
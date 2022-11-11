def hangman(motdevine):
    rep = []
    for i in range(len(motdevine)):
        if i == len(motdevine)-1:
            rep.append("_")
        else:
            rep.append("_")
            rep.append(" ")
    guesses = 0
    fail = []
    while True:
        guesses += 1
        letter = input("Entrez votre lettre\n")
        if letter in fail or letter in rep:
            print("Cette lettre à déjà été utilisée")
        else:
            
            guess = False
            for i in range(len(motdevine)):
                if letter == motdevine[i]:
                    rep[i*2] = letter
                    guess = True
            if guess:
                print("Vous avez trouvé la lettre " + letter + "\n")
            else:
                print("Cette lettre n'est pas bonne\n")
                fail.append(letter)
            word = ""
            correct = ""
            for i in rep:
                word += i
                if i != " ":
                    correct += i
            if correct == motdevine:
                break
            else:
                print(word)
    return "Vous avez trouvé le mot " + motdevine + " avec " + str(guesses) + " essais"
mot = input("Entrez le mot à faire deviner\n")
for i in range(0,20):
    print("\n")
print(hangman(mot))
        
        
        
        
import random as rd
def eightball():
    liste = ["Bien sur que non!","Mais oui !","Vas-y !","Je ne pense pas",
             "Je ne suis pas de cette idée","Je suis totalement d'accord","Je pense que oui",
             "J'en suis sur","Je ne crois pas","Ce n'est pas mon avis"]
    
    return liste[rd.randint(0,len(liste)-1)]
q = input("Posez votre question, on vous répondra avec intérêt\n")
print(eightball())

        
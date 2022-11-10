def dectohex(entry):
    
    table = {
        0:'0',
        1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9',
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F',
        }
    
    entry = int(entry)
    ans = ""
    while entry > 0:
        ans = ans + str(table[entry%16])
        entry = entry//16
    return ans[::-1]
dec = input("Entrez un nombre décimal\n")
print(dectohex(dec))
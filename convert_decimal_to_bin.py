def dectobin(entry):
    entry = int(entry)
    ans = ""
    while entry > 0:
        ans += str(entry%2)
        entry = entry//2
    return ans[::-1]
dec = input("Entrez un nombre décimal\n")
print(dectobin(dec))
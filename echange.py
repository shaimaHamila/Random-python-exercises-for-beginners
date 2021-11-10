ch = input("saisir votre mots : ")
first = ch[0]
last = ch[-1]
mot = last + ch[1: len(ch)] + first
print(mot)

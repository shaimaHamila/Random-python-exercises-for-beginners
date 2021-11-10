mot = input("Saisire un mot : ")
inverse = ""
for i in range(len(mot)-1, -1, -1):
    inverse = inverse + mot[i]

print(f"L'inverse du {mot} est : {inverse}")
# ou bien
# obtenir l'inverse de la chaine s
# s1 = s[::-1]

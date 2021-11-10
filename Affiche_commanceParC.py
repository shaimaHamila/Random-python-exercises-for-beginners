texte = (input("saisire un text : ")).split(' ')

for mot in texte:
    if mot[0] == 'a':
        print("Le mot : ", mot, " commence par la lettre 'a'")


# deuxiemme methode

# Lire la chaine s
s = input("Tapez une chaine de caractères s : ")

# convertir la chaine s en une liste
s = s.split()

# obtenir la longueur de la liste s
n = len(s)

# rechercher les éléments de la liste qui commencent par la lettre 'a'
for i in range(0,n):
     if(s[i][0] == 'a'):
         print("Le mot : '", s[i], "' commence par la lettre 'a'")
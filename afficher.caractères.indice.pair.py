def index_pair(mot):
    ch = ''
    for i in mot:
        if mot.index(i) % 2 == 0:
            ch = ch + i
    print(ch)


mot = input("saisir um mot : ")
index_pair(mot)

#Autre methode
mot = input("saisir um autre mot : ")
print(mot[0: len(mot): 2])



s = "Python est un langage de programmation. Python est orienté objet"

# Transformation de la chaine s en une liste
L = s.split()

# Récupération du nombre d'élément de la liste L
nombreMots = len(L)
print("Le nombre de mot de la chaine s est : ", nombreMots)
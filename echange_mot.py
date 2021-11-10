s = "Python est un langage de programmation"

# Transformation de la chaine s en une liste L
L = s.split()

# Récupération du nombre d'élément de la liste L
n = len(L)

# récupération du premier et dernier élément
premier = L[0]
dernier = L[n-1]

# On supprime le premier et le dernier élément de la liste L
L.pop()
L.pop(0)

# On reconvertit la liste L en une chaine
s1 = " ".join(L)

# échanger le premier et le dernier élément dans la chaine s
s = dernier + " " + s1 + " " + premier
print(s)


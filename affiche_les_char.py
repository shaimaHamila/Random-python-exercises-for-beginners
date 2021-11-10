s = input("donner votre mots : s =  ")
unique = ""
for i in s:
    if i not in unique:
        unique += i
        print(f"le caractere : > {i} >> figure {s.count(i)} fois dans la chaine s  ")

"""""
 #autr methode
 #regrouper les caractères de s dans un ensemble pour éviter les répetitions
unique =set({})
for x in s:
    if x not in unique:
       unique.add(x)
        print("Le nombre d'occurrences du caractère: ", x, " dans la chaine s est :", s.count(x))
"""""

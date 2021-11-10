Voyelles = ['a', 'i', 'o', 'y', 'e', 'u']
ch = input("donnez votre mot : ")
Nombre_voyelle = 0
for i in range(0, len(ch)):
    for voyelle in Voyelles:
        if ch[i] == voyelle:
            Nombre_voyelle = Nombre_voyelle + 1


print(f"La chaine {ch} possède {Nombre_voyelle} voyelles. ")

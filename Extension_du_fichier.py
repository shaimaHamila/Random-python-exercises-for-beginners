Fichier = input("Donnez le nom du fichier : ")
l = Fichier.split(".")
NomFichier = "." + l[-1]

print(f"L'extension du fichier est {NomFichier}")
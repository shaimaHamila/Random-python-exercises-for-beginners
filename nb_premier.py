nombre = int(input("saiser le nombre : "))
premier = bool
premier = 1
diviseur = ""
for i in range(2,nombre):
    if nombre % i == 0:
        premier = 0
        diviseur += str(i) + ", "
if premier == 1:
    print(f"{nombre} est un nombre premier ")
else:
    print(f"{nombre} n'est pas premier et il est diviser par : {diviseur} ")

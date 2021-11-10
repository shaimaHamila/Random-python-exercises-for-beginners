entier = int(input("donnez un entier : "))
diviseur = 1
for diviseur in range(1, entier + 1):
    if entier % diviseur == 0:
       print(diviseur)

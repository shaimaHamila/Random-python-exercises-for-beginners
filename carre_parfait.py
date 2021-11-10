nombre = int(input("saisire votre nombre : "))
test = bool
test = 0
for i in range(1, nombre//2 + 1):
    if i**2 == nombre:
        test = 1

if test == 1:
    print(f"{nombre} est un  carre parfait ")
else:
    print(f"{nombre} n'est pas un carre parfait")
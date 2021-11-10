def somme(liste):
    s = 0
    for i in range(len(liste)):
        s = s + liste[i]
    return s


def produit(liste):
    p = 1
    for i in liste:
        p = p*i
    return p


liste = [5, 8, 8, 3, 4]
print(f"La somme egale : {somme(liste)}")
print(f"Le produit egale : {produit([5, 8, 8, 3, 4])}")

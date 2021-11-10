def lesMotsCommun(l1, l2):
    global commun
    l1 = l1.split()
    l2 = l2.split()
    motsCommun = []
    for commun in l1:
        if commun in l2:
            motsCommun.append(commun)
    return motsCommun


s1 = " Python est un langage de programmation de haut niveau"
s2 = " Python est un langage interprété"
print("La liste des mots communs à s1 et s2 est : ", lesMotsCommun(s1, s2))
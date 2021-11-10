def paire_impair(list):
    list_pair = []
    list_impair = []
    for i in list:
        if i % 2 == 0:
            list_pair.append(i)
        else:
            list_impair.append(i)
    print(f"La liste des entiers paire est : {list_pair}")
    print(f"La liste des entiers impaire est : {list_impair}")


liste = [23, 4, 56, 7, 8, 9, 0, 18, 7, 6, 55, 43, 2]
paire_impair(liste)

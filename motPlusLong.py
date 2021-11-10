def motsLong(list):
    list = list.split()
    long = 0
    for longMot in list:
        if long < len(longMot):
            long = len(longMot)
    motsLong = []
    for mot in list:
        if long == len(mot):
            motsLong.append(mot)
    return motsLong


ch = "hello chaima hamila"
print(f"Les mots les plus long dans la chaine s est : {motsLong(ch)} ")
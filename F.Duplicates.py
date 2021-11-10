def remove_duplicates(numbers):
    for duplicate in numbers:
        if numbers.count(duplicate) > 1:
            numbers.remove(duplicate)
    return numbers


liste = [1, 1, 2, 2, 3, 4, 4, 4, 5]
print(liste)
print(remove_duplicates(liste))

# Autre methode

def removeDuplicates1(lists):
    unique = []
    for duplicate in lists:
        if duplicate not in unique:
            unique.append(duplicate)
    return unique


lists = [2, 2, 2, 5, 5, 8, 9, 5, 5, 5, 9, 8]
print(lists)
print(removeDuplicates1(lists))

# Autre methode

# définir la fonction qui supprie les élément dupliqués d'une liste
def removeDuplicate(l):
    # convertir la liste en un ensemble
    SET = set(l)
    # reconvertir l'ensemble en une liste
    L   = list(SET)
    return L

# Exemple
l = [2, 7,7, 13, 2, 17,25, 17, 13, 15, 15, 2, 7, 13]
print(removeDuplicate(l))
"""
importation du module itertools:
Ce module implémente de nombreux blocks d'itérateurs inspirées des constructions APL, Haskell et SML.
"""
import itertools

# Example d'utilisation
l = [1, 2]
permutations = itertools.permutations(l)
L = list(permutations)
print("Les listes obtenues en échangeant les termes de la liste l:\n", L)

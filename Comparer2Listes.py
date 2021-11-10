def elementsCommun(liste1, liste2):
    elements = []
    for element in liste1:
        if (element in liste2) and (element not in elements):
            elements.append(element)

    return elements


liste1 = [1, 1, 2, 2, 3, 4, 4, 4, 5]
liste2 = [2, 2, 2, 5, 5, 8, 9, 5, 5, 5, 9, 8]
print(f"Les elements commun entre la liste 1 {liste1} et la liste 2 {liste2} sont : {elementsCommun(liste1, liste2)}")
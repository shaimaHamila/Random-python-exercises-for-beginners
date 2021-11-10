number = [1, 6, 5, 1, 6, 5, 8, 9, 8, 8]
for duplicates in number:
    if number.count(duplicates) > 1 :
        number.remove(duplicates)
print(number)
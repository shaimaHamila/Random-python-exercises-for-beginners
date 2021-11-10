Mot = input("Donnez un mot : ")

for i in range(0, len(Mot)//2 + 2):
    if Mot[i] == Mot[len(Mot)-1-i]:
        test = 1
    else:
        test = 0

if test == 1:
    print(f"{Mot} est un Palindrome ")
else:
    print(f"{Mot} est n'est pas un Palindrome ")

#ou bien
# inverser le mot
#inverse = mot[::-1]
#if(mot == inverse):
 #   print("Le mot :", mot," est un palindrome")
#else:
 #   print("Le mot : ", mot, " n'est pas un palindrome")
l = 'hello      chaima     hamila     .'
s = l.split()
textSansEspace = ""
for x in s:
    textSansEspace = textSansEspace + x + " "

print(f"Le texte avec les espaces : {l} \nLe texte sans les espaces : {textSansEspace}")


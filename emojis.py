
def emojis_converter(message):
    words = message.split(' ')
    emojis={
             ":)" : "🙂",
             ":(" : "☹",
             ":|" : "😐",
              ";)" : "😉",
             ":*" : "😘",
             "<3" : "❤"

    }
    output =''
    for word in words :
        output += emojis.get(word, word)+ " "
    return output


message = input('>')
print(emojis_converter(message))




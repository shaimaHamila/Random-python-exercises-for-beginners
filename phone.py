numbers ={
    '1': 'one',
    '2': 'tow',
    '3': 'three',
    '4': 'four',
    '5': 'fife',
    '6': 'six',
    '7': 'seven',
    '8': 'eght',
    '9': 'nine',
    '0': 'zero'
}
phone = input('phone ')
phone_number =''
for number in phone :
   phone_number += numbers.get(number, '!')+' '
print(phone_number)

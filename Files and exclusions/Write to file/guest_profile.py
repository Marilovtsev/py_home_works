filename = 'guest.txt'

text = '\nEnter "stop" to exit.'
text += '\nHi! Tell me your name: '

while True:
    name = input(text)
    if name == 'stop':
        break

    else:
        print('\nHello ' + name.title() + '!')
        reason = input('Why do you like programming: ')
        with open(filename, 'a') as guest_data:
            guest_data.write(f'\nThe reason why {name.title()} is like programming: {reason.capitalize()}')
            break

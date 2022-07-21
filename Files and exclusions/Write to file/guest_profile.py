filename = 'guest.txt'

text = '\nEnter "stop" when you are finished.'
text += '\nHi! Tell me your name: '

while True:
    name = input(text)
    if name == 'stop':
        break
    else:
        print('Hello ' + name.title() + '!')
        with open(filename, 'a') as guest_data:
            guest_data.write(f'\n{name.title()}')

from random import choice

numbers = 'A 1 B 2 C 3 4 5 D 6 7 8 E 9 10'.split()
print('Win ticket = ' + choice(numbers) +
      ' ' + choice(numbers) +
      ' ' + choice(numbers) +
      ' ' + choice(numbers))

from random import choices


def get_random_ticket():
    s = '0123456789abcde'
    return choices(s, k=4)


win_ticket = get_random_ticket()
print('Выигрышным является билет с комбинацией:', *win_ticket)
i = 1
while get_random_ticket() != win_ticket:
    i += 1
print(f'Для получения выигрышной комбинации понадобилось {i} итераций.')

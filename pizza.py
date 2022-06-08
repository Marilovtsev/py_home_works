def make_pizza(size, *topings):
    """Выводит описание пиццы."""
    print(f"\nMaking a {size}-ich pizza with the folowing toppings:")
    for toping in topings:
        print(f'- {toping}')

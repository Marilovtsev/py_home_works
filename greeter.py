def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформитированное полное имя"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last Name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# # first function
# def greet_user():
#     print("Hello!")
#
#
# greet_user()
#
#
# # Transfer of information for function 1.0
# def greet_user(username):
#     print(f"Hello, {username.title()}!")
#
#
# greet_user('jesse')
#
#
# # Transfer of information for function 1.1
# def display_message(information):
#     print(f"Argument and {information.title()} - this is theme of this Paragraph")
#
#
# display_message('parametrs')
#
#
# # Favorite book function
# def favorite_book(book):
#     print(f"One of my favorite books is {book.title()}!")
#
#
# favorite_book('the witcher')
#
#
# # Position arguments
# def describe_pet(animal_type, pet_name):
#     """Print information about pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet('hamster', 'harry')
#
#
# # Многократные вызовы функций
# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')
#
#
# # Именованные аргументы
# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet(animal_type='hamster', pet_name='harry')
#
#
# # Значения по умолчанию
# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet(pet_name='willie')
#
#
# # function make_shirt 1.0
# def make_shirt(size_shirt, print_text):
#     print(f"Your company have a new task!")
#     print(f"Shirt size - {size_shirt.title()}, text on the shirt - '{print_text}'.")
#
#
# make_shirt('s', 'Hello World!')
# make_shirt(size_shirt='xl', print_text='Python it`s cool!')
#
#
# # function make_shirt 1.1
#
# def make_shirt(size_shirt='L', print_text='I love Python!'):
#     print(f"Your company have a new task!")
#     print(f"Shirt size - {size_shirt.title()}, text on the shirt - '{print_text}'.")
#
#
# make_shirt()
# make_shirt(size_shirt='xxl', print_text='Python it`s best of the best!')
#
#
# # function describe_city
#
# def describe_city(city_name, country_name='Ukraine'):
#     print(f"{city_name.title()} is in {country_name.title()}")
#
#
# describe_city('kharkiv')
# describe_city(city_name='kharkiv')
# describe_city(city_name='krakov', country_name='poland')
#
#
# # Return value
#
# # def get_formatted_name(first_name, last_name):
# #     """Возвращает аккуратно отформатированное полное имя,"""
# #     full_name = f"{first_name} {last_name}"
# #     return full_name.title()
# #
# #
# # musician = get_formatted_name('glen', 'miller')
# # print(musician)
#
# # Необязательные аргументы функции
#
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)
#
# def build_person(first_name, last_name):
#     """Возвращает словарь с информацией о человеке."""
#     person = {'first': first_name, 'last': last_name}
#     return person
#
#
# musician = build_person('jimi', 'hendrix')
# print(musician)


# def build_person(first_name, last_name):
#     """Возвращает словарь с информацией о человеке."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)



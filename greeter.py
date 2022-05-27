# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформитированное полное имя"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == "q":
#         break
#     l_name = input("Last Name: ")
#     if l_name == "q":
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# Location name function
def city_country(city, country):
    format_city_country = f"{city}, {country}"
    return format_city_country.title()


location = city_country("kharkiv", "ukraine")
location_1 = city_country("krakow", "poland")
location_2 = city_country("paris", "france")
print(location)
print(location_1)
print(location_2)


# Album function
def get_make_album(artist_name, album_name):
    album = {"Artist": artist_name, "Album": album_name}
    return album


while True:
    print("\nPlease tell me Artist:")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist name: ")
    if artist_name == "q":
        break
    album_name = input("Album name: ")
    if album_name == "q":
        break
    make_album = get_make_album(artist_name, album_name)
    print(f"\nResult: {make_album}!")

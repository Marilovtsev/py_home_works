from Admin import Admin

my_admin = Admin("Збигнев", "Бзежински", 29, "newadmin@admin.com")
my_admin.describe_user()

new_admin_privileges = ['разрешено добавлять сообщения',
                        'разрешено удалять пользователей',
                        'разрешено банить пользователей']
my_admin.privileges.privileges = new_admin_privileges

print("\nАдминистратор " + my_admin.last_name + " имеет следующие привелегии: ")
my_admin.privileges.show_privileges()

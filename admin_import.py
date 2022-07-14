from user_profile_3 import Admin

new_admin = Admin("Elon", "Musk", 41, "tesla@spacex.com")
new_admin.describe_user()

new_admin_privileges = ['разрешено добавлять сообщения',
                        'разрешено удалять пользователей',
                        'разрешено банить пользователей']
new_admin.privileges.privileges = new_admin_privileges

print("\nThe admin " + new_admin.last_name + " has these privileges: ")
new_admin.privileges.show_privileges()

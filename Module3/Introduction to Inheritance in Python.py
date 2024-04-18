"""
One of the fundamental tenants of object-oriented programming in any language is the concept of inheritance.
At a high level inheritance is the ability to create specialized versions of classes.
"""


class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'


class AdminUser(User):
    def active_users(self):
        return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.active_users())
print(tiffany.greeting())
print(kristine.greeting())
#print(kristine.active_users()) # burada hata aliriz
#kristine nin active user fonksiyonuna erisimi yoktur ama tiffani user class ina inherite ettigi icin icerisindeki fonksiyonlarada erisimi vardir


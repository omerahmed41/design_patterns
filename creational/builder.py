from abc import ABC, abstractmethod


class IPersonBuilder(ABC):

    @abstractmethod
    def build(self):
        """"""


class Person:
    name = None
    age = None
    address = None
    role = 'client'

    def __str__(self):
        return f'person: {self.role}- {self.name} - {self.age} - {self.address}'


class PersonBuilder(IPersonBuilder):

    def __init__(self):
        self.person = Person()

    def set_name(self, name):
        self.person.name = name
        return self

    def set_age(self, age):
        self.person.age = age
        return self

    def set_address(self, address):
        self.person.name = address
        return self

    def set_role(self, role):
        self.person.role = role
        return self

    def build(self):
        return self.person


class AdminDirector:
    @staticmethod
    def construct():
        return PersonBuilder().set_role('admin').set_name('Admin').build()


class UserDirector:

    @staticmethod
    def construct():
        return PersonBuilder().set_role('client').set_name('normal_user').build()


if __name__ == '__main__':
    admin = AdminDirector.construct()
    user = UserDirector.construct()

    print(admin)
    print(user)

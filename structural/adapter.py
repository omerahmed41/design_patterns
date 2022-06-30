
from abc import ABCMeta, abstractstaticmethod


class IA(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_age():
        ''''''
class A():
    @staticmethod
    def get_age():
        return '20'

class B():
    @staticmethod
    def get_age():
        return 20

class Adapter():
    def __init__(self,cls: IA) -> None:
        self.cls = cls

    def get_age(self):
        return str(self.cls.get_age())

class Printer():

    def __init__(self, age):
            self.age = age
    def __str__(self) -> str:
        return 'age is ' + self.age

if __name__ == '__main__':
    age = Adapter(B).get_age()
    p = Printer(age)
    print(p)
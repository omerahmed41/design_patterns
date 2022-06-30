from abc import ABCMeta, abstractstaticmethod

class Person():

    name = None 
    age = None 
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def __str__(self):
        return f'{self.name} is {self.age}'

class PersonDecorator(Person):
    def __init__(self,person:Person):
        self.person = person
    def __getattr__(self, name: str):
        return getattr(self.person, name)

    def __str__(self):
        if self.person.age >= 18:
            return (f'Young: {self.person}')
        else:
            return (f'Child: {self.person}')



if __name__ == '__main__':
    omer = Person('Omer', 20)
    ali = Person('Ali', 10)
    print(omer)
    print(PersonDecorator(omer))
    print(ali)
    print(PersonDecorator(ali))


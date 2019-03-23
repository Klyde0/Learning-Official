# Person class with name attribute and talk() method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


person1 = Person('John')
bob = Person('Bob Smith')

print(person1.talk())
print(bob.talk())
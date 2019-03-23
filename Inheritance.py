# Inheritance = Mechanism for reusing code
# Say you define a class with its own methods and you define another class
# It would be painstaking to rewrite all the same code for that other class
# Solution = we define a new class that is a parent of dog and cat class
# so now when we create subclasses of mammal, we can do Subclass(ParentClass)
# every method in the ParentClass is now inherited by the Subclass
# The subclass can also have its own methods unique to the Subclass + methods of Parentclass
# If theres no other unique methods, type in pass

class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark'
        )


class Cat(Mammal):
    def meow(self):
        print('meow')


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.walk()
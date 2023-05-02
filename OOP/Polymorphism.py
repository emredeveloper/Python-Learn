class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def move(self):
        print(f"{self.name} is moving")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

    def wag_tail(self):
        print(f"{self.name} is wagging its tail")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")

    def scratch(self):
        print(f"{self.name} is scratching")


class Hayvan(Dog):

    def __init__(self,isim):
        super().__init__(isim)



    def durum(self):
        hayvan.eat()
        hayvan.sleep()
        hayvan.move()
        hayvan.bark()
        hayvan.wag_tail()



""""
def main():
    # Create some animals
    dog = Dog("Sparky")
    cat = Cat("Mittens")

    # Make the animals do things
    dog.eat()
    dog.bark()
    dog.wag_tail()

    cat.eat()
    cat.meow()
    cat.scratch()
"""

dog = Dog("Kangal")


hayvan = Hayvan("Pitbull")
print(hayvan.durum())

# hayvan.durum(dog)

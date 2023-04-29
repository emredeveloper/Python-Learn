class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self) -> object:
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
class Hayvan:
    def hayvan(self, hayvan: Animal):
        print("Hayvanın ismi: ", hayvan.name)
        print(hayvan.name+"'ın yemek metodu: ", hayvan.eat())
        print(hayvan.name+"'ın sleep metodu: ", hayvan.sleep())
        print(hayvan.name+"'ın move metodu: ", hayvan.move())


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

dog = Dog("Kangal")

if __name__ == "__main__":
    main()
hayvan = Hayvan()
hayvan.hayvan(dog)
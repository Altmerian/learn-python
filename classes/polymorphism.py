class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Cat: {self.name}. Age: {self.age}")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Dog: {self.name}. Age: {self.age}")

    def make_sound(self):
        print("Woof")


if __name__ == "__main__":
    cat = Cat("Whiskers", 2)
    dog = Dog("Buddy", 3)

    animals = [cat, dog]

    for animal in animals:
        animal.info()
        animal.make_sound()

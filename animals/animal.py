class Animal:
    def __init__(self, name="Garfield", age=0):
        self.name = name
        self.age = age

    def talk(self):
        print(f"My name is {self.name}")


    def say_age(self):
        print(f"I'm {self.name}.")
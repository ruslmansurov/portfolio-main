from animal import Animal

class Dog(Animal):
    def __init__(self, name, age, breed="Underfined"):
        Animal.__init__(self, name, age)
        self.breed = breed

    def run(self):
        print(f"I'm is running")


    def talk(self):
        print("Gav, ", end="")
        Animal.talk(self)
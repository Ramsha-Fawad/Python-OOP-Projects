class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Woof! My name is {self.name}!")

dog1 = Dog("Jackie", "German Shepherd")

dog1.bark() 

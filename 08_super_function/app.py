class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

teacher1 = Teacher("Mr. Sarfraz", "Chemistry")

teacher1.display_info()
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public variable
        self._salary = salary       # Protected variable
        self.__ssn = ssn            # Private variable

    # Getter and Setter for public variable (name)
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    # Getter and Setter for protected variable (_salary)
    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
        else:
            print("Salary cannot be negative!")

    # Getter and Setter for private variable (__ssn)
    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, new_ssn):
        if isinstance(new_ssn, str) and len(new_ssn) == 11:
            self.__ssn = new_ssn
        else:
            print("Invalid SSN format!")


# Create object
emp = Employee("Rosina", 50000, "123-45-6789")

# Access using getters
print("Name:", emp.get_name())
print("Salary:", emp.get_salary())
print("SSN:", emp.get_ssn())

# Modify using setters
emp.set_name("Jasmine")
emp.set_salary(60000)
emp.set_ssn("987-65-4321")

# Access updated values
print("\nAfter updates:")
print("Name:", emp.get_name())
print("Salary:", emp.get_salary())
print("SSN:", emp.get_ssn())

class Employee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")


class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        # Aggregation: employee is passed as a reference
        self.employee = employee

    def display_department_info(self):
        print(f"Department: {self.dept_name}")
        print("Employee working in this department:")
        self.employee.display_info()


# Create an Employee object (exists independently)
emp1 = Employee(101, "Ramsha Fawad", "Software Engineer")

# Create a Department object and pass the employee object to it
dept1 = Department("IT", emp1)

# Display information
dept1.display_department_info()

# Demonstrating that emp1 still exists independently of dept1
print("\nAccessing Employee independently:")
emp1.display_info()

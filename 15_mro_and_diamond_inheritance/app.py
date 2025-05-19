class A:
    def show(self):
        print("Show method from class A")

class B(A):
    def show(self):
        print("Show method from class B")

class C(A):
    def show(self):
        print("Show method from class C")

class D(B, C):  # Multiple Inheritance
    pass

# Create an object of class D
d = D()

# Call the show method
d.show()

# Display Method Resolution Order
print("\nMethod Resolution Order (MRO):")
for cls in D.__mro__:
    print(cls)
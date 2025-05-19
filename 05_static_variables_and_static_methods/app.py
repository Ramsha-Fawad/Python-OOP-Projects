class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


# Using the static method without creating an object
result1 = MathUtils.add(5, 7)
result2 = MathUtils.add(-3, 10)
result3 = MathUtils.add(0, 0)

# Displaying the results
print("Sum of 5 and 7 is:", result1)
print("Sum of -3 and 10 is:", result2)
print("Sum of 0 and 0 is:", result3)

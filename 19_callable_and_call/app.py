class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an instance of Multiplier
double = Multiplier(2)

# Test with callable()
print(callable(double))  # Output: True

# Call the object like a function
result = double(10)
print(result)

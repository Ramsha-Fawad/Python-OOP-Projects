class Logger:
    def __init__(self):
        print("Logger object created!")

    def __del__(self):
        print("Logger object destroyed!")


# Creating an object of Logger class
print("Creating logger1...")
logger1 = Logger()

# Deleting the object manually
print("Deleting logger1...")
del logger1

# Wait to show that the program continues after deletion
print("Program continues after object destruction...")

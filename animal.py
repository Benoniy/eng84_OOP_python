# Create first class
# class - used to create a class

# This is how you create a class
class Animal:
    # name = "dog"  # Class variable

    def __init__(self):  # Initialization class analogous to a constructor (builds the object)
        # Attributes / Instance variables
        self.alive = True
        self.spine = True

    def move(self):
        return "I move"


if __name__ == "__main__":
    animal = Animal()  # This is abstraction
    print(animal.alive)

# How does inheritance work
# See reptile.py

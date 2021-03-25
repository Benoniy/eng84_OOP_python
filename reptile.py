# Import the animal class
from animal import Animal


class Reptile(Animal):  # Inheritance is done this way, parent classes are args

    def __init__(self):
        super().__init__()  # Perform the same initialization as the parent class
        self.cold_blooded = True
        self.hibernate = None

    def shed(self):
        return "shedding"


if __name__ == "__main__":
    reptile_obj = Reptile()
    print(reptile_obj.move())  # Use of an inherited method (DRY)


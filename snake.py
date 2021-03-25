from reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.hibernate = True  # You can override values of the parent class, this is polymorphism
        self.forked_tounge = True

    def smell(self):
        return "Use tounge to smell"


if __name__ == "__main__":
    cobra = Snake()
    # Multiple inheritance
    print(cobra.move())  # Inherited from Animal class
    print(cobra.shed())  # Inherited from Reptile class
    print(cobra.smell())  # Not inherited from any class

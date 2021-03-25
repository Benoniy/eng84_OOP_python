# A display of multiple inheritance
from reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tounge = True
        self.venom = True

    def smell(self):
        return "Use tounge to smell"


if __name__ == "__main__":
    cobra = Snake()
    # Multiple inheritance
    print(cobra.move())  # Inherited from Animal class
    print(cobra.shed())  # Inherited from Reptile class
    print(cobra.smell())  # Not inherited from any class

from snake import Snake


class Adder(Snake):

    def __init__(self):
        super().__init__()
        self.venom = False  # You can override values of the parent class, this is polymorphism


if __name__ == "__main__":
    bob = Adder()
    print(bob.venom)

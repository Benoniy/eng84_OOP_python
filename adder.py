from snake import Snake


class Adder(Snake):

    def __init__(self):
        super().__init__()
        self.venom = False  # You can override values of the parent class, this is polymorphism

    def smell(self):  # You can also override the method of the parent class, this is polymorphism
        return "I smell but like an adder"


if __name__ == "__main__":
    bob = Adder()
    print(bob.venom)
    print(bob.smell())

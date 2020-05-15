class M3GTR:
    def __init__(self, colour, price):
        self.name = "BMW M3 GTR"
        self.year = 2020
        self.colour = colour
        self.price = price

    def print_details(self):
        print("Name: ", self.name)
        print("Year: ", self.year)
        print("Colour: ", self.colour)
        print("Price: ", self.price)

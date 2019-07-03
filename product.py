
class Product:
    'Common base class for all events'

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.price == other.price

    def __gt__(self, other):
        """Override the default behavior"""
        return self.price > other.price

    def __lt__(self, other):
        """Override the default behavior"""
        return self.price < other.price

    def display_product(self):
        print( self.name," ", self.price)
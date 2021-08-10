class Coffee:
    def __init__(self):
        self._milk = 'Milk'
        self._icecream = 'Icecream'
        self._espresso = 'Espresso'
        self._water = 'Water'
        self._cinnamon = 'Cinnamon'

    def latte(self):
        return self._espresso + ' & ' + self._milk

    def cappuccino(self):
        return self._espresso + ' & ' + self._milk + ' & ' + self._cinnamon

    def glace(self):
        return self._espresso + ' & ' + self._icecream

    def americano(self):
        return self._espresso + ' & ' + self._water

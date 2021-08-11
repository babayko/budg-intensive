class Coffee:
    def __init__(self, ingridients):
        self.__dict__.update(ingridients)

    @classmethod
    def latte(cls, **kwargs):
        return cls(ingridients=kwargs)

    @classmethod
    def cappuccino(cls, **kwargs):
        return cls(ingridients=kwargs)

    @classmethod
    def glace(cls, **kwargs):
        return cls(ingridients=kwargs)

    @classmethod
    def americano(cls, **kwargs):
        return cls(ingridients=kwargs)

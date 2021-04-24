from abc import ABC, abstractmethod


class Clothes(ABC):
    total = 0

    @abstractmethod
    def expense(self):
        pass

    @staticmethod
    def total_cost():
        return f'Общий расход ткани: {Clothes.total:.2f} м2'


class Coat(Clothes):

    def __init__(self, name, V):
        self.name = name
        self.V = V

    @property
    def expense(self):
        result = self.V/6.5 + 0.5
        Clothes.total += result
        return f'Расход ткани на пальто: {self.name} {result:.2f}'


class Suit(Clothes):

    def __init__(self, name, H):
        self.name = name
        self.H = H

    @property
    def expense(self):
        result = 2 * self.H + 0.3
        Clothes.total += result
        return f'Расход ткани на костюм: {self.name} {result:.2f}'


a = Coat('Tommy Hilfiger', 200)
print(a.expense)
print(Clothes.total_cost())
b = Suit('Louis Vuitton', 300)
print(b.expense)
print(Clothes.total_cost())
c = Coat('Tommy Hilfiger', 300)
print(c.expense)
print(Clothes.total_cost())
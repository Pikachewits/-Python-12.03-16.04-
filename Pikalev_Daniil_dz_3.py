class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        result = self.number - other.number
        if result > 0:
            return Cell(self.number - other.number)
        else:
            raise Exception(f'Разность чисел меньше нуля')

    def __str__(self):
        return str(self.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def __truediv__(self, other):
        return Cell(self.number / other.number)

    def make_order(self, count):
        full_rows = self.number // count
        row = f'{"*" * count} \n' * full_rows + f'{"*" * (self.number % count)}'
        return row

cells_1 = Cell(23)
print(cells_1.make_order(5))
print(cells_1)
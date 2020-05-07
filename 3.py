#Задание 3




class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __str__(self):
        if self.cells >= 0:
            if self.cells >= 1:
               cells_str = self.cells * '*'
            else:
                cells_str = 'В зародыше'
        else:
            cells_str = 'Клетки в в другом измерении'

        return f'Клеточки --> {cells_str}, ({self.cells})'

    def __add__(self, other):
        new_cells = self.cells
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        minus_cells = self.cells - other.cells
        if minus_cells > 0 :
            otv = minus_cells * '*'
        else:
            otv = ('!Маловато будет!')
        return f'Клеточки --> {otv}, ({minus_cells})'


    def __mul__(self, other):
        umn_cells = self.cells * other.cells
        return Cell(int(umn_cells))

    def __truediv__(self, other):
        del_cells = round(self.cells // other.cells)
        return Cell(del_cells)


    def make_order(self, cells_in_str):
        otv = ''
        for i in range(int(self.cells / cells_in_str)):
            otv += f'{"*" * cells_in_str} \n'
        otv += f'{"*" * (self.cells % cells_in_str)}'
        return otv

cells1 = Cell(5)
cells2 = Cell(20)

print(cells1)
print(cells2)

print(cells1 + cells2)
print(cells2 - cells1)
print(cells1 - cells2)

print(cells2.make_order(5))
print(cells1.make_order(12))

print(cells1 / cells2)
#Задание 2




class Textil:

    def __init__(self, value, height):
        self.value = value
        self.height = height



    def square_coat(self):
        return self.value / 6.5 + 0.5



    def square_jacket(self):
        return self.height * 2 + 0.3



    @property
    def full_square(self):
        full_sqr = round((self.value/ 6.5 + 0.5) + (self.height * 2 + 0.3), 2)
        return str(f'Общая площадь ткани составляет: {full_sqr} ')



class Coat(Textil):
    def __init__(self, value, height):
        super().__init__(value, height)
        self.square_c = round(self.value / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто {self.square_c}'




class Jacket(Textil):
    def __init__(self, value, height):
        super().__init__(value, height)
        self.square_j = self.height * 2 + 0.3



    def __str__(self):
        return f'Площадь ткани на костюм {self.square_j}'



coat = Coat(2, 4)
jacket = Jacket(1, 2)

print(coat)
print(jacket)

print(coat.full_square)
print(jacket.full_square)

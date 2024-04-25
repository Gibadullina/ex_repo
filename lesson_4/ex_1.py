class BaseFigure:
    def get_info(self):
        print(self.square, self.perimeter)


class Square(BaseFigure):
    def __init__(self, a):
        self.square = a * a
        self.perimeter = 4 * a


rectangle = Square(9)

rectangle.get_info()


class Square2:
    def __init__(self, length):
        self.length = length

    def get_perimeter(self):
        print(f'Периметр: {self.length*4}')

    def get_square(self):
        print(f'Площадь: {self.length*self.length}')


sq = Square2(4)
sq.get_square()
sq.get_perimeter()

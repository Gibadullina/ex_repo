class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        print(f'Сумма: {self.num1 + self.num2}')

    def subtraction(self):
        print(f'Разница: {self.num1 - self.num2}')

    def multiplication(self):
        print(f'Умножение: {self.num1 * self.num2}')

    def division(self):
        print(f'Деление: {self.num1 / self.num2}')


calc = Calculator(4, 4)
calc.addition()


from datetime import date
today = date.today()


class Human:
    def __init__(self, name, city, year_bd):
        self.name = name
        self.city = city
        self.year_bd = year_bd

    def get_age(self):
        print(f'Возраст: {today.year - self.year_bd}')


woman1 = Human('Helen', 'New York', 2001)
woman1.get_age()

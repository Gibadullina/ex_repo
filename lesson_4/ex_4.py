class Kitty:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


my_kitty = Kitty('Mao')
print(my_kitty)

print('\nПример без метода __str__:')
class Dog:
    def __init__(self, name):
        self.name = name


my_dog = Dog('Zoe')
print(my_dog)

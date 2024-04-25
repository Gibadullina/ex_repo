# Пример миксинов
class Mixin:
    def mixin_method(self):
        return "Mixin method called"


class MyClass(Mixin):
    pass


obj = MyClass()
print(obj.mixin_method())

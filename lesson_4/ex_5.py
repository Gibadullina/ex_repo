from random import randint


class Employee:
    def __init__(self, salary):
        self.salary = salary

    @classmethod
    def get_paid(cls):
        s = cls(randint(50000, 100000))
        return s


class Worker(Employee):
    pass


class Manager(Employee):
    pass


analyst = Worker.get_paid()
pm = Manager.get_paid()

print(analyst.salary)
print(pm.salary)

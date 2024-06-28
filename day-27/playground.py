def add(*args):
    for n in args:
        n += n - 1 + n
    return n


print(add(1, 3, 5, 7, 9, 11, 13, 15))


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(n=2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Ford")
print(my_car.make)
print(my_car.model)

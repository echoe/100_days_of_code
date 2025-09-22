def add(*args):
    result = 0
    for n in args:
        result += n
    return result

print(add(20,5,15,7))

# def calculate(**kwargs):
#     """You can handle these kwargs in so many ways"""
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
#     print(kwargs["add"])

# calculate(add=3, multiply=5)

def calculate(n, **kwargs):
    """You can handle these kwargs in so many ways"""
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# class Car:
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#     def print(self):
#         print(self.make, self.model)

# my_car = Car(make="Honda", model="Corolla")
# print(my_car.model)
# my_car.print()

# my_half_car = Car(make="Fiat")
# print(my_half_car.model)

# If you want to dodge the KeyError this creates you can use .get() to have it auto-fill 'None' if there is nothing
# matching a query in the keyword arguments dictionary:

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
    def print(self):
        print(self.make, self.model)

my_car = Car(make="Honda", model="Corolla")
print(my_car.model)
my_car.print()

my_half_car = Car(make="Fiat")
print(my_half_car.model)
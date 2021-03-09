# 1. Create a Vehicle class with max_speed and mileage instance attributes


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have
# seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        self.seating_capacity = seating_capacity
        super().__init__(max_speed, mileage)

    def seating_capacity(self):
        return self.seating_capacity()


# 3. Determine which class a given Bus object belongs to (Check type of an object)

bus = Bus(150, 2000, 50)
print(type(bus))

# output:
# <class '__main__.Bus'>

# 4. Determine if School_bus is also an instance of the Vehicle class

School_bus = Bus(130, 3500, 80)
print(isinstance(School_bus, Vehicle))

# output:
# True

# 5. Create a new class School with get_school_id and number_of_students instance attributes


class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_id(self):
        print(f'School id is {self.get_school_id}.')


school = School(12345, 2000)
school.school_id()

# output:
# School id is 12345.

# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have
# its own - bus_school_color


class SchoolBus(School, Bus):
    def __init__(self, school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances,
# one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

class Bear:
    def make_sound(self):
        print('Argh')


class Wolf:
    def make_sound(self):
        print('Awoo')


bear = Bear()
wolf = Wolf()

for animals in (bear, wolf):
    animals.make_sound()


# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        print(f'Creating the city {name}')
        city = super(City, cls).__new__(cls)
        if population > 1500:
            return city
        else:
            return 'Your city is too small'

# 9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}

    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'


city_1 = City('Big_city', 700000)
print(city_1)
city_2 = City('Small_city', 1300)
print(city_2)

# output:
# Creating the city Big_city
# The population of the city Big_city is 700000
# Creating the city Small_city
# Your city is too small

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is
# greater than 10. And perform this add (+) of two instances.


class SumNum:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        if self.num > 10:
            return self.num * other.num
        else:
            return self.num + other.num


num_1 = SumNum(3)
num_2 = SumNum(25)

print(num_1 + num_2)
print(num_2 + num_1)

# output:
# 28
# 75

# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and
# can be called like a function.
# Create a new class with __call__ method and define this call to return sum.


class CallMethod:
    def __call__(self, *args):
        return sum(args)


method_1 = CallMethod()
print(method_1(5, 10))
print(method_1(5, 10, 15))
print(method_1(5, 10, -15, -20))

# output:
# 15
# 30
# -20

# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False


class MyOrder:
    def __init__(self, card, customer):
        self.card = card
        self.customer = customer

    def __bool__(self):
        return True if len(self.card) != 0 else False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')

print(bool(order_1))
print(bool(order_2))


# output:
# True
# False

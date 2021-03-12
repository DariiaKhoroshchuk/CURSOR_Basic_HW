import dataclasses
import collections


# 1.
class Laptop:
    """
    Make the class with composition.
    """
    def __init__(self):
        battery_1 = Battery('Energy of battery_1')
        battery_2 = Battery('Energy of battery_2')
        self.batteries = [battery_1, battery_2]


class Battery:
    """
    Make the class with composition.
    """
    def __init__(self, energy):
        self.energy = energy


# 2.
class Guitar:
    """
    Make the class with aggregation
    """
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    """
    Make the class with aggregation
    """
    def __init__(self):
        pass


guitar_string_1 = GuitarString()
guitar_1 = Guitar(guitar_string_1)

# 3


class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """
    total_calc = 0

    def __init__(self, num):
        self.num = num
        Calc.total_calc = Calc.total_calc + num

    @classmethod
    def add_nums(cls):
        print(f'Total sum: {cls.total_calc}')


num_1 = Calc(5)
num_2 = Calc(3)
num_3 = Calc(8)

Calc.add_nums()


# output:
# Total sum: 16


# 4*.

class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
pasta_2 = Pasta.bolognaise()

print(pasta_1.ingredients)
print(pasta_2.ingredients)

# output:
# ['tomato', 'cucumber']
# ['bacon', 'parmesan', 'eggs']


# 5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, count):
        self._visitors_count = count if count <= self.max_visitors_num else self.max_visitors_num


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

# output:
# 50


# 6.

@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str),
    birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


John = AddressBookDataClass(123, 'John', '87654321', 'Saharova, 15', 'john@gmail.com', '12,03,1999', 21)
print(John)
print(John.email)

# output:
# AddressBookDataClass(key=123, name='John', phone_number='87654321', address='Saharova, 15', email='john@gmail.com',
# birthday='12,03,1999', age=21)
# john@gmail.com

# 7. Create the same class (6) but using NamedTuple

AddressBookDataClass1 = collections.namedtuple('AddressBookDataClass1', ['key', 'name', 'phone_number', 'address',
                                                                         'email', 'birthday', 'age'])
Anna = AddressBookDataClass1(234, 'Anna', '12345678', 'Soborna, 10', 'anna@gmail.com', '19,06,2000', 20)
print(Anna)
print(Anna[5])
print(Anna.address)

# output:
# AddressBookDataClass1(key=234, name='Anna', phone_number='12345678', address='Soborna, 10', email='anna@gmail.com',
# birthday='19,06,2000', age=20)
# 19,06,2000
# Soborna, 10


# 8.

class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBookDataClass(key={self.key}, name={self.name}, phone_number={self.phone_number}, ' \
               f'address={self.address},email={self.email}, birthday={self.birthday}, age={self.age}'


Oskar = AddressBook(key=345, name='Oskar', phone_number='1234964', address='Gorodska, 3', email='oskar@gmail.com',
                    birthday='26,03,2001', age=19)
print(Oskar)

# output:
# AddressBookDataClass(key=345, name=Oskar, phone_number=1234964, address=Gorodska, 3,email=oskar@gmail.com,
# birthday=26,03,2001, age=19


# 9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person = Person()
print(person.age)
person.age = 20
print(person.age)

# output:
# 36
# 20


# 10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    # attribute of the class
    student_id = 0
    name = ""

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


student = Student(1, 'John')
setattr(student, 'email', 'john@gmail.com')
print(student.email)
student_email = student.__getattribute__('email')
print(getattr(student, 'email'))
print(student_email)

# output:
# john@gmail.com
# john@gmail.com
# john@gmail.com

# 11*.


class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """
    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def fahrenheit(self):
        return (self.temperature * 1.8) + 32


# create an object
fahrenheit_temp = Celsius(33)
print(fahrenheit_temp.fahrenheit)

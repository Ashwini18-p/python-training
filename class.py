#class is a blueprint or template to create a object
class Student:      #student which is a class name
    name = "Aswini"
    company = "LetitbexAI"
    age = 24
s1 = Student()  #student() where we created a object
print(s1.name)
print(s1.company)
print(s1.age)
#object is a instance of class
#class with multiple objects
class Student:
    name = "Aswini"
    company = "LetitbexAI"
    age = 25
s1 = Student()
s2 = Student()
s3 = Student()
print(s1.name)
print(s1.company)
print(s1.age)
print(s2.name)
print(s2.age)
print(s2.company)
print(s3.name)
print(s3.company)
print(s3.age)  

#class attributes are inside a class , but outside methods
class Student:
    college = "SEAT college"
    course = "Python"
s1 = Student()
s2 = Student()
print(s1.college)
print(s2.college)
print(Student.course)

#instance attributes belongs to individual objects
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = student("Ash", 24)
s2 = student("likky", 23)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)

#methods A method is a function defined inside a class methods means actions or behaviour
class Student:
    def study(self):
        print("student is studying")
    def play(self):
        print("student is playing")
s1 = Student()
s1.study()
s1.play()

#A constructor is a special method that is automatically called when a object  is created. it is used to initialize the object attributes
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("Ash", 24)
print(s1.name)
print(s1.age)

class Student:
    def __init__(self, name, age):
        print("constructor executed")  # two times will get call because we created object for 2 times
        self.name = name
        self.age = age
s1 = Student("Ash", 24)
s2 = Student("likky", 25)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)

#self method is a reference to the current object of a class.it is used to access instance attributes and instance methods.
class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
s1 = Student("Aswini")
s1.display()

#@class method means it is used to represent to class
class Student:
    company = "letitbexai"
    @classmethod
    def show_company(cls):
        print(cls.company)
Student.show_company()

#@static method doesn't use cls or self
class Math:
    @staticmethod
    def add(a, b):
        return a + b
print(Math.add(10, 20))

#encapsulation means wrapping attributes and methods into single unit called as class
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def show_balance(self):
        print(self.__balance)
account = BankAccount(5000)
account.deposit(2000)
account.show_balance()

#inheritance is a mechsanisam where one classacquires the properties and methods of another class
class Parent:
    def house(self):
        print("parent has a house")
class Child(Parent):
    def car(self):
        print("child has a car")
c1 = Child()
c1.house()
c1.car()

#polymorphism means one name many forms means same method name but in different classes and different behaviour we can provide
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("cat meow")
class Cow:
    def sound(self):
        print("cow mooo")
d = Dog()
c = Cat()
co = Cow()
d.sound()
c.sound()
co.sound()

#types of inheritance 
#there are  types of inheritances
#single inheritance one parent class one child class
class Aswini:
    def working_in(slef):
        print("LetitbexAI")
class Company(Aswini):
    def Who_is_working(self):
        print("Aswini")
working = Company()
working.working_in()
working.Who_is_working()

#multiple inheritance a child can inherit from one or more parent classes
class Father:
    def father_property(self):
        print("A father has a assets")
class Mother:
    def mother_property(self):
        print("A mother has a gold")
class child(Father, Mother):
    def child_property(self):
        print("A child has bike and all his parents assets")
c = child()
c.father_property()
c.mother_property()
c.child_property() 

#multilevel inheritance means inheritance happens in multilevel like a chain
class Grandfather:
    def property(self):
        print("he has a land")
class Father(Grandfather):
    def prop(self):
        print("he has a house")
class child(Father):
    def pro(self):
        print("he has a bike")
c = child()
c.property()
c.prop()
c.pro()

#Method overriding is the process of redefining a parent class method in a child class with the same method name
class Father:
    def phone(self):
        print("father uses samasung")
class Son(Father):
    def phone(self):
        print("son uses i phone")
c = Son()
c.phone()
f = Father()
f.phone()

#super() function is used to acess methods from parent class inside the child class
class Father:
    def phone(self):
        print("father uses samasung")
class Son(Father):
    def phone(self):
        super().phone()
        print("son uses i phone")
c = Son()
c.phone()

#hierarichal inheritance one parent class and multiple child classes can use the parent class
class Father:
    def land(self):
        print("i has a land")
class Son(Father):
    def bike(self):
        print("i has a bike")
class Daughter(Father):
    def gold(self):
        print("i has a gold")
class Anotherson(Father):
    def prop(self):
        print("i had nothing")
s = Son()
d = Daughter()
a = Anotherson()
s.land()
s.bike()
d.land()
d.gold()
a.land()
a.prop()

#dunder methods to define how objjects behave with normal operations
#__int__() constructor when we create the objects it automatically calls
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Aswini")
print(s1.name)

#__str__() it is a string representation when we print the objects it gives in a readble format
class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
s1 = Student("Aswini")
print(s1.name)

#__len__ when we call the length on object it will get call
class Student:
    def __init__(self, names):
        self.names = names
    def __len__(self):
        return len(self.names)
s1 = Student(["Aswini", "LIkky", "teju"])
print(len(s1))

#__add__ when the + operator is used b/n the two objects
class Numbers:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
n1 = Numbers(10)
n2 = Numbers(20)
print(n1 + n2)

#__eq__ when == two objectes are compared then it will get call
class Numbers:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value == other.value
n1 = Numbers(10)
n2 = Numbers(20)
print(n1 == n2)

#dataclasses automatically assigns a constructors in the code we dont need to explicitly write the constructors in code
#normal class
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
s1 = Student("aswini", 24, "Python")
print(s1.name)
print(s1.age)
print(s1.course)

#with @dataclass decorator 
from dataclasses import dataclass
@dataclass
class Student:
    name : str
    age : int
    course : str
s1 = Student("aswini", 24, "python")
print(s1)

#default values means when we re creating a object that time we dont assign the values 
from dataclasses import dataclass
@dataclass
class Student:
    name : str
    age : int = 24
    course : str = "python" 
s1 = Student("Ash")
print(s1)

#field() it gives additional settings to the atributes
from dataclasses import dataclass, field
@dataclass
class Student:
    name : str
    age :int
    course : list = field(default_factory = list)
s1 = Student("Aswini", 24)
s2 = Student("likky", 24)
s1.course.append("python")
print(s1.name)
print(s1.age)
print(s1.course)
print(s2.name)
print(s2.age)
print(s2.course) 

#frozen dataclasses means immutable once we created the object we cant modify the values
from dataclasses import dataclass
@dataclass(frozen= True)
class Student:
    name : str 
    age : int
s1 = Student("Aswini", 24)
# s1.age = 25   #gives frozeninstanceerror
print(s1)
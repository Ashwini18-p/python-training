#nested function a function is defined inside an another function and inner function should call inside outer function
def outer_function():
    def inner_function():
        print("Hi this is inner function inside outer function")
    inner_function()
outer_function()

#if we dont call the inner function inside the outer function then we will get the error
# def outer():
#     def inner():
#         print("inner")
# outer()
# inner()

#real time example
def login():
    print("user login started")
    def passowrd():
        print("passowrd entered")
    passowrd()
login()

#closures means after the completion of outer function the inner function still remember the values of outer function
def outer():
    message = "hello"
    def inner():
        print(message)
    return inner
result = outer()
result()

#decorator is a function that takes another function as an argument adds extra functionality to it, and return a function without modifying the original function
def decorator(func):
    def decoration():
        print("print it before execution")
        func()
        print("print it after execution")
    return decoration
@decorator #here we re decorating to the first function without modifying the original function
def greet():
    print("hello Aswini")
greet()

#decorators with arguments
def aswini(func):
    def wrapper(name):
        print("before execution")
        func(name)
        print("after execution")
    return wrapper
@aswini
def greet(name):
    print("Hello", name)
greet("Aswini Padileti")

#functools.wraps it is a decorator it is used inside another decorators to preserve the original functions meta  data
#without functools
def decorator(func):
    def decoration():
        print("print it before execution")
        func()
        print("print it after execution")
    return decoration
@decorator 
def greet():
    """This is a greeting function"""
    print("hello Aswini")
greet()
print(greet.__name__)
print(greet.__doc__)

#with functools
from functools import wraps
def decorator(func):
    @wraps(func)
    def decoration():
        print("print it before execution")
        func()
        print("print it after execution")
    return decoration
@decorator 
def greet():
    """This is a greeting function"""
    print("hello Aswini")
greet()
print(greet.__name__)
print(greet.__doc__)
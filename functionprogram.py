#using map printing square of numbers map function is used to apply a function to every element in an iterable
numbers = [1, 2, 3, 4, 5]
def square(n):
    return n * n
result = map(square, numbers)
print(list(result)) # here very function is applied to an iterable

#using lambda
numbers = [1, 2, 3, 4, 5]
result = map(lambda x:x * 2, numbers)
print(list(result))   # here every element is multiplied by 2

#filter function is used to filter elements from an iterable based on a given condition it sends 
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = filter(lambda x:x % 2 == 0, numbers)
print(list(result))

#reduce that repeatedly  applies a function to the elements of a sequence and reduce them into a single variable
from functools import reduce
nums = [ 1, 2,  3, 4]
result = reduce(lambda a , b : a*b, nums)
print(result)

#a first class function means a function can be treated as any other object in python
#function assigned to  a variable
def greet():
    return "hello"
assigned = greet
print(greet())

#passing function as an argument
def greet():
    return "hi"
def display(func):
    print(func())
display(greet)

#returning a function from other function
def outer():
    
 def inner():
    return "hi this is inner function returning to outer function"
 return inner
x = outer()
print(x())


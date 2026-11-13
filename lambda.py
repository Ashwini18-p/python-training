#normal function
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

#anonymous(defined using  lambda keyword) function this function has no name and can take multiple arguments and take single expresiion
square = lambda x: x * x
print(square(7))

add = lambda a, b: a + b
print(add(30, 40))

#lambda with three arguments 
add = lambda a, b, c : a + b + c
print(add(10,20,30))

#lambda with no arguments
text = lambda : "hello this is aswini"
print(text())

#lambda expression is a expression written after a : in a function
add = lambda a ,b : a + b  # this is lambda expression

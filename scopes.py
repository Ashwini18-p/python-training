#variables means where we can access the variable from which part of a program
#local scope
def local_scope():
    name = "aswini"
    age = 24
    print(name, age)         #here print is inside the same function so we can access if we access outside the function it gives an error
local_scope()  

#what if print is accessed outside the function
# def local_scope():
#     name = "aswini"
#     age = 24            
# local_scope() 
# print(name, age)

#global scope it can be accessed inside and outside of the function it can be declare inside and outside of the function
name = "Aswini"
def global_scope():
    age = 24
    print(name, age)
global_scope()
print(name)
#suppose if we want to change the value inside the global variable
x = 10
def modify():
    x = 20
    print(x)
modify()
print(x)

#we can modify it using global keyword
x = 10
def modify():
    global x
    x = 20
    print(x)
modify()
print(x)

#nonlocalvalue this keyword is used to modify a variable belonging to the nearest enclosing function
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20
        print("Inner:", x)
    inner()

    print("Outer:", x)
outer()

#without nonlocal keyword  it doesnot change the value
def outer():
    x = 10

    def inner():
        
        x = 20
        print("Inner:", x)
    inner()

    print("Outer:", x)
outer()

#LEGB rule
x = "outer"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
outer()

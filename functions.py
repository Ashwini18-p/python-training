#without function
a = 10
b = 20
print (a + b)

x = 10
y = 20
print (x + y)

#with function 
def add ():
    a = 10
    b = 20
    print(a + b)
add()  
add() #we wrote addition logic here one time but we call the function 2 times

#function definition - it is used to define or create the function to define the function we use def keyword
#calling a function
def greet():
    print("hello world!")  #creating a function means it wont execute the program

def greet():
    print("hello world!") #now it executes the function because here we re calling a function
greet()

#parameters and aruguments
def add(a, b):  #these are the parameters
    print(a + b)
add(10 , 20) #these are the arguments 

#return values is a keyword it sends a result from function back to the place where function was called
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

#return with multiple values 
def maths(a , b):
    addition = a + b
    subtraction = a - b
    return addition , subtraction
result = maths(25, 55)
print(result)

#without return it shows the none with print bcoz print does not send a result
def add(a, b):
    print (a + b)
result = add(10, 20)
print(result)
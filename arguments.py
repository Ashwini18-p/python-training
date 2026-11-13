#positional arguments these are arguments passed to a function based on the position
def positional(name, age):
    print("name:", name)
    print("age:", age)
positional("aswini", 24)  #it passes the values to the variables based on the position if we change the positional the values also changes

#changing the arguments so that values may vary
def positional(name, age):
    print("name:", name)
    print("age:", age)
positional(24, "Aswini")

#keyword arguments these are the arguments this pass the values by explicitly adding parameters names along with the values
def student_details(name, age, course):
    print("name:", name)
    print("age:", age)
    print("course:", course)
student_details(name = "aswini", age = 24, course = "python")

def student_details(name, age, course):
    print("name:", name)
    print("age:", age)
    print("course:", course)
student_details(age = 24, name = "aswini", course = "python")  #if we change the arguments also the output comes with the parameters

#default arguments are the arguments where the values are passed alonh with the parameters when calling the function definition
def default_args(name = "Aswini", age = 24):
    print("name:", name)
    print("age", age)
default_args()
#if we give arguments while calling the function the default arguments wont work
def default_args(name = "Aswini", age = 24):
    print("name:", name)
    print("age", age)
default_args(name = "likky")

#*args this allows a function to accept number of positional arguments 
#normal without *args
def args(a, b):
    print(a + b)
args(1, 2)   # these take two arguments only without *args

#with *args
def args(*args):
    print(args)
args(1, 2, 3, 4, 5)
#to find max number
def args(*args):
    print(max(args))
args(1, 2, 3, 4, 5)

#**kwargs allows a function to accept number of keyword arguments in a dictionary
def kwargs(**kwargs):
    print(kwargs)
kwargs(name = "Aswini", age = 24, course = "python")

#iteration in **kwargs
def kwargs(**kwargs):
    for key, values in kwargs.items():
        print(key, ":", values)
kwargs(name = "Aswini", age = 24, course = "python")
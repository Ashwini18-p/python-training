#exception handling is used to handle runtime errors without terminating the program
# a = 10
# b = 0
# result = a / b
# print(result)

#try block means when we re excepting if the error occurs that code we will write in try block 
# try :
#     a = 10
#     b = 0
#     result = a / b
#     print(result) 
# finally:
#     print("not executed") #writing try block means exception handling is not fulfilled
#except block is used to handle the exception that occurs iin try block
try :
    a = 10
    b = 0
    result = a / b
    print(result)
except:
    print("something weent wrong")

#else block executes when no exception occurs in try block
try :
    a = 10
    b = 20
    result = a / b
    print(result)
except:
    print("something weent wrong")
else:
    print("Result:", result)

#finally blockis used in exception handling it contains code that will always execute. whether an exception occurs or not
try :
    print(10/0)
except ZeroDivisionError:
    print("cannot divided by zero")
finally:
    print("this is always run")

    #raise is a keywors we manually creating an errors
try:
    age = 15
    if age < 18:
        raise ValueError("Age must be 18 or above")
except ValueError as e:
    print("error:", e)
finally:
    print("verification completed")

#custom exceptions python has some built in exceptions if we want some exceptions that are related to the application then we user defines the exception based on we need
#we have to use use raise keyword for trigger
class AgeError(Exception):
    pass
try:
    age = 15
    if age < 18:
        raise AgeError("Age must be18 or above")
        print("you can vote")
except AgeError as e:
    print(e)
#file handling means storing data in files and will do some operations like writing reading modifying etc
#file opening and reading
file = open ("datatypes.py", "r")
data = file.read()
print(data)
file.close()
#reading methods read() completely reads the content
#readline() only reads one line
file = open ("datatypes.py", "r")
data = file.readline()
print(data)
file.close()  

#rreadlines() return the content in list
file = open ("datatypes.py", "r")
data = file.readlines()
print(data)
file.close()

#file writing() wites the content and existing content will get delete
# file = open ("datatypes.py", "w")
# file.write("hi")
# file.close()

#fileappending() it adds the content at the end it wont delete existing data
file = open ("datatypes.py", "a")
file.write("\n #numbers")
file.close()

#file modes x - mode
#it creates a new file 
# file = open("module.py", "x")
# file.write("hello ash")
# file.close()

#r+ mode do read and write operation
#a+ mode do reading and writing operations
#with statement - whenever we opens the files sometimes we may forgot to close the files to automatically close the files we use with statement()
with open("datatypes.py", "r") as file:
    data = file.read()
    print(data)
#encoding in python we use utf - 8 in python it will english , telugu , special symbols will support
with open("moodule.py", "w", encoding="utf-8") as f:
    f.write("హలో అస్విని")


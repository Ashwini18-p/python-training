#f string is used to embed the variables or expressions with {}
employee = "aswini" 
age = 24
print(f"welcome to letitbexai {employee} and she is {age} years old")

#expressions inside f string 
a = 10
b = 20
print (f"after adding two numbers :{a+b}")

#input function
name = input("enter your name :")
print(name)

#firstly python gives any input value as str so we can use like this
age = int(input("enter age here :"))
print (age)
print (type(age))

#the int age became as str
age = input("enter age here :")
print (age)
print (type(age))

#print function
print ("hello world")
print ("welcome to letitbe")
print (10.5)
print (20)

# we can print multiple values
print ("hi welcome to the world", "i welcomed you to this world")
#2
name = "aswini"
age = 24
print ("my name is",name)
print ("my age is",age)

#we can use seperator so what we wanna show between the values
name = "aswini"
age = 24
print ("my name is ", name , "my age is", age, sep= "|")
#2 using --
name = "aswini"
age = 24
print ("my name is ", name , "my age is", age, sep= "--")

# end parameter
print ("hello world", end =" ")
print ("is my world")

print ("hello world", end =" ")
print ("is my world", end ="         ")
print ("om sairam")

#string formatting by f string
employee = "aswini"
company_name = "letitbexai"
print (f"here is {employee} she is working in {company_name}")
#string format using by .format
employee = "aswini"
company_name = "letitbexai"
print ("here is {} she is working in {} ".format(employee,company_name))


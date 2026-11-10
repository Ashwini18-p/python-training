#simple type conversion
a = "10"
print (type(a))

#converting str into int

a = "10"
b = int(a)
print (type(b))

#implicit type conversion where the program itself converts
a = 10
b = 10.5
c = a + b
print (c)
print(type(c)) #it converts into float only

a = 10
b = 10.5
d = 10+5j
c = a + b + d
print (c)
print(type(c))

a = 10
b = 10
c = a / b
print (c)
print(type(c))   #division opeartor in python it converts into a float 

#explicit conversion where a developer converts the data type
#interger string to float
a = "10"
b = float(a)
print (type(b))

#string with decimal to integer
a = "10.5"
result = int(float(a)) #in python we can only convert like this
print (result)

#integer to float
a = 10
b = float(a)
print (b)
print (type(b))

#integer to complex
a = 10
b = complex(a)
print (b)
print (type(b))

#boolean to integer
a = 1
b = 0
c = bool(a)
d = bool(b)
print(c)
print(d)
print (type(c))

#string to integer
a = "10"
result = int(a)
print (result)
print (type(result))

#float to integer
a = 10.5
result = int(a)
print (result)
print (type(result))

#float to cpmplex
a = 10.5
result = complex(a)
print (result)
print (type(result))

#float to str
a = 10.5
result = str(a)
print (result)
print (type(result))

#list to tuple
a = [1,2,3]
result = tuple(a)
print (type(result))
print (result)

#tuple to list
a = (1,2,3,4)
result = list(a)
print (type(result))
print (result)

#string to list
a = "Aswini"
result = list(a)
print (type(result))
print (result)
#string to tuple
a = "Aswini"
result = tuple(a)
print (type(result))
print (result)

#list to string
a = ['a', 'b', 'c']
result = str(a)
print (type(result))
print (result)



# a small scenario
employee_name = "Aswini"
employee_age = "10"
monthly_salary = 300000
anual_salary = monthly_salary * 12
age_into_int = int(employee_age)
salary_into_float = float(monthly_salary)
print ("Employee_name:", employee_name)
print ("Employee_age:", employee_age)
print ("montly_salary:", monthly_salary)
print (age_into_int)
print (salary_into_float);print (anual_salary)

#isinstance
a = 10
b = "aswini"
c = 10.5
d = 10+5j
e = [1,2,3,4]
f = (1,2,3,4)
print (isinstance(a,float))
print (isinstance(b,str))
print (isinstance(c,float))
print (isinstance(d,complex))
print (isinstance(e,list))
print (isinstance(f,tuple))
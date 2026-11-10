#Arthimetic Operators
a = 10
b = 20
print(a + b)
print(a - b)
print(a // b) # returns an integer
print(a / b) # returns an float
print(a * b)
print(a ** b)
print(a % b)

#2 
a = 10
b = 20
c = a - b 
print (c)

#Comparision operator
if 10 > 5:
    print(True)
else:
    print(False)

#2
a = 10
b = 20
print (a > b)
print (a < b)
print (a == b)
print (a != b)
print (a >= b)
print (a <= b)

#logical operators
a, b, c = True, False, True

if a and c:
    print("Both a and c are True .")

if b or c:
    print("Either b or c is True .")

if not b:
    print("b is False .")

#assignment operator which asigns the values
#basic =
a = 10
#+ assignment
a = 10
a += 5
print (a)

# - assigment
a = 10 
a -= 5
print (a)

# % assignemnt
a = 10
a %= 5
print(a)

#* assigment 
a= 10
a *= 5
print (a)

#/ assignment
a = 10
a /= 5
print(a)

#membership operator both in and not in for tuples
fruits = ("apple", "banana", "jack")
print ("apple" in fruits)
print ("orange" in fruits)
print ("orange" not in fruits)

#membership operator both in and not in for string
employee = "aswini in letitbe"
print ("aswini" in employee)
print ("in" not in employee)

#membership operator both in and not in for list
avacado = ["jack", "ram", "rom"]
print ("we" in avacado)
print ("jack" not in avacado)

#comparision
a = 10
b = 10 
print (a == b )
print (a != b)

#identify operator is and is not
a = [10,20,30]
b = [10,20,30]
print (a is b)
print (a is not b)


#1
a = 25
b = 4
c = a % b
print(c)
#2
a = int(input("enter first number"))
b = int(input("enter second number"))
c = a ** b
print ("the final exponential number is:", c)
#3
age = 18
if age >= 18:
    print("you re eligible to the vote")
else:
    print("you re not eligible")
#4
fruits = ["apple", "banana", "jack", "mango","musa"]
print ("mango" in fruits)
#5
fruits =[1,2,3,4]
mango = [1,2,3,4]
print(fruits == mango)
print (fruits is mango)

#logical operator and
a = 18
print (a >=20 and a <=60)

#or
a = 18
print (a >=20 or a <=60)

#not
is_rainy = True
print(not is_rainy)

is_rainy = False
print(not is_rainy)

#bit wise operators
a = 10
b = 20
print (a & b) #and operator

a = 10
b = 20
print (a | b) #or operator

a = 10
b = 20
print (a ^ b) #xor operator

a = 5
print(~a) #bitwise not operator

a = 8
print (a >> 1) #leftshift
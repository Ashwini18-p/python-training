#commemts are generally used for understanding like we developers knowing what tis this meant for
#this is string data type

#indentations
number = 5
if number < 10:
    print ("yes 5 is less than 10")
else:
    print ("no 5 is not less than 10")
    
#identifiers
#Valid identifiers:
# var1
# _var1
# _1_var
# var_1
# Invalid Identifiers

# !var1
# 1var
# 1_var
# var#1
# var 1

#identifiers 
employee = 10 #employee is an identifier

import keyword
print(keyword.kwlist)

#without indentation
# a = 10
# b = 20
# if a > b:
# print ("a is gretaer than b")

#with indentation

if 10 > 20:
    print ("20 is greater than 10")


#2 
age = 22
if age >= 18:
    print ("you are eligible to vote")
else:
    print ("you are an adult")
print ("complete the process")

age = 22
if age >= 18:
    print ("you are eligible to vote")
    if age >= 28:
        print ("you are an adult")
print ("complete the process")


#multi line indentation
age = 18
if age >= 18:
    print ("you are eligible to vote")
    if age <= 18:
        print("not eligible")

#identifiers can casesensitive
Many = "fuits"
MANY = "banana"
   
    
 
   
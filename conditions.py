#if statement only executes the block of code when the specified condition is true
age = 20
if age <= 22 :
    print("you can apply for visa.")
else:
    print("you cannot")
#2
age = 20
if age >= 18:
    print("Eligible to vote.")

#if the if condition is false if there is no else or elif stmts it skips the block
age = 20
if age <= 22 :
    print("you can apply for visa.")

#3 single hand if we cant print in a single line
age = 20
if age >= 18: print("Eligible to vote.")

#else stmt
age = 20
if age >= 22:
    print("you can pay for ticket")
else:
    print("you can go free")

#elif is used to check multiple conditions when the first conditions are false

marks = 80
if marks >= 95:
    print("you are first")
elif marks >= 100:
    print("you are second place")
elif marks >= 75:
    print("you are third")
else:
    print("you are fail")

#if the elif conditions also false it returs else
marks = 80
if marks >= 95:
    print("you are first")
elif marks >= 100:
    print("you are second place")
elif marks <= 75:
    print("you are third")
else:
    print("you are fail")

#4
electricity_units = 100
if electricity_units >= 200 :
    print("you can have free access")
elif electricity_units >= 150:
    print("you can have free access.")
elif electricity_units >= 110:
    print("you can have free access.")
elif electricity_units >= 80:
    print("you will not have free access.")
else:
    print("you may go")

#if inside if means nested if statements
bill_should = 150
electricity_bili = 100
if bill_should >= 100:
    if electricity_bili >= 100:
        print("you can apply for free access")
else:
    print("you afre not eligible")
print ("suceess you may go")

#conditional expressions
age = 16
result = "adult" if age >= 18 else "minor"
print(result) 


        
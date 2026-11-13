#normal for loop
numbers = [1,2,3,4,5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)

#using list comprehension- it is also used to create a collection like a loop but in comprehension we write a simple line code
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)          #both give same output only but the code is short

#to print 1 to 5 numbers using comprehension
digits = [x for x in range(1,6)]
print(digits)

#to print square numbers 
numbers = [1, 2, 3, 4, 5]
value = [x ** 2 for x in numbers]
print(value)

#converting strings to uppercase
names = ["aswini", "likitha", "tejaswi"]
result = [name.upper() for name in names]
print(result)

#creating dictionary with comprehension
names = ["ashu", "likki", "teju"]
ages = [23, 24, 25]
result = {name: age for name, age in zip(names, ages)}
print(result)

#set comprehensions
#removing duplicate values
dup_numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
result = {x for x in dup_numbers}
print(result)

#creating a set of squares
numbers = [1, 2, 3, 4, 5]
result = {x ** 2 for x in numbers}
print(result)
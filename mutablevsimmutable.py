#mutability where we can change the value of an object after the creation without creating a new object
numbers = [10, 20, 30, 40]
print(numbers)
numbers[0] = 100
print(numbers)

#immutable means we cant change the value once after it created we can only create a new object
name = "aswini"
name = "python"
print(name)

numbers = 10
numbers = numbers + 5
print(numbers)

#object references python dont store the actual data instead it stores the references means address of the object in a memory
a = [10, 20, 30]
b = a
print(a)
print(b)

#modifying b so that a also will change
a = [10, 20, 30]
b = a
b [1] = 200
print(a)
print(b)

#we can check object reference of a value using id()
a = [10, 20, 30]
b = a
print(id(a)) #both will be same bcoz nboth values refer to same
print(id(b))

a = [10, 20, 30] #different reference number
b = [20,60]
print(id(a))
print(id(b))

#shallow copy creates a new outer object but the elements iside it are referenced to the original object
import copy
a = [10, 20, 30, 40]
b = copy.copy(a)
print(a)
print(b)
#modifying b
import copy
a = [10, 20, 30, 40]
b = copy.copy(a)    #seperate object changing the outerlist value doesnot affetct the original
b [0] = 20
print(a)
print(b)

#nested list
import copy
a = [[10, 20 ], [30, 40]]
b = copy.copy(a)
print(a)
print(b)

#modifying b
import copy
a = [[10, 20 ], [30, 40]]
b = copy.copy(a)
b [0][0] = 100 #the value changes for both 
print(a)
print(b)

#deep copy 
import copy
a = [[10, 20 ], [30, 40]]
b = copy.deepcopy(a)
print(a)
print(b)
#modifying b
import copy
a = [[10, 20 ], [30, 40]]
b = copy.deepcopy(a)
b[0][0] = 100
print(a)
print(b)
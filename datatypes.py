#simple practicing program
a = 10
b = "aswini"
c = 10.5
d = 10+5j
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#none 
employee_name = None
print(type(employee_name))
print(employee_name)

#string type
employee_name = "aswini"
print (employee_name)
print (type(employee_name))

#can be accessed using index
print (employee_name[1])
print (employee_name[-1])

#string with indexing 
name = "aswini"
age = "24"
company_name = "letitbexai"
print(name)
print(age)
print(company_name)
print(name[3])
print(age[1])
print(type(name))

#string slicing
name = "python"
print(name[0:4])
print(name[1:5])
print(name[:])
print(name[:5])
print(name[1:])

#negative slicing
name = "python"
print(name[-4:-1])

#string methods
name = "python programming"
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.replace("python", "java"))
print(name.startswith("python"))
print(name.endswith("gramming"))

#list data type
s = [1]
print(type(s))
d = ["pen", "for", "book", 4, 5]
c = ["blue for red"]
print(type(d))
print(c[-1])
print(d[1])

#list with different data type
names = ["fruits", 10 , 23.5]
#list slicing ruleslike string
number = [10, 20, 30, 40, 50, 60]
print(number[0:4])

#tuple data type
t1 = (1,)
print(type(t1))

t2 = ('red', 'For', 'pink', 1, 2)
print(t2[3])
print(t2[-3])

#dictionary data type
d = {1: 'employee', 2: 'aswini', 3: 12345}
print(d[1])    
print(d.get(2))

#boolean data type
a = 10
b = 20
print (a > b)
print (a < b)
print (a == b)
print (a != b )
#2
employee_name = True
employee_name1 = False
print(type(employee_name))

#dynamic typing
x = 42
print(type(x)) # <class 'int'>

x = "Dynamic Typing"
print(type(x)) # <class 'str'>

x = [1, 2, 3]
print(type(x)) # <class 'list'>
print (x)

#list methods
a = [1 , 2, 3, 4, 5]
a.append(6)
print (a)

#insert
a = [1 , 2, 3, 4, 5]
a.insert(4, 6)
print (a)

#extend
a = [1 , 2, 3, 4, 5]
b = [6,7,8,9]
a.extend(b)
print (a)

#reverse
a = [1 , 2, 3, 4, 5]
a.reverse()
print (a)

#pop specific
a = [1 , 2, 3, 4, 5]
a.pop(3)
print (a)

#pop
a = [1 , 2, 3, 4, 5]
a.pop()
print (a)

#clear
a = [1 , 2, 3, 4, 5]
a.clear()
print (a)

#sets
a = {1,2,3,4,5,2,1,3,3,4,5}
print(a)
print(type(a))

#set methods add
a = {1,2,3,4}
a.add(6)
print(a)
#update 
a = {1,2,3,4,}
a.update([6,5,7,8,6,6])
print(a)
#remove if the element doesnot exist it sends an error
a = {1,2,3,4}
a.remove(4)
print(a)
#discard if the element doesnot exist it wont show error
a = {1,2,3,4,}
a.discard(3)
print(a)

#tuple methods count
a = (1,2,3,4,5)
print(a.count(3))
#index
a = (1,2,3,4,5)
print(a.index(4))

#dictionary 
name = {
    "name" : "aswini",
     "age" :23,
     "employee" : "details"
}
print(name)
print(type(name))

# range represents a sequence of integers
numbers = range(1,6)
print (list(numbers))
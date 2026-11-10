#creation of lists
employee = ["Aswini", 10, 10.5, 10 + 5j]
print(employee)
print(type(employee))

#lists indexing
employee = ["Aswini", 10, 10.5, 10 + 5j]
print(employee[1]) #positive indexing
print(employee[0])
print(employee[-1]) #negative indexing
print(employee[-3])

#list slicing same as like strings
employee = ["Aswini", 10, 10.5, 10 + 5j]
print(employee[0:2])
print(employee[-3:-1])

#list methods
employee = ["Aswini", 10, 10.5, 10 + 5j]
employee.append(35) #append adds an element end of the list
print(employee)
#2
employee = ["Aswini", 10, 10.5, 10 + 5j]
bus = [10, 20, 30]
employee.extend(bus)#extend which adds multiple elements at the end of the list
print(employee)
#3
employee = ["Aswini", 10, 10.5, 10 + 5j]
employee.reverse() #reverse the list
print(employee)
#4
employee = [ 10, 10.5, 10, 50]
employee.sort()
print(employee)
#5
employee = ["Aswini", 10, 10.5, 10 + 5j]
employee.clear()#clears the list 
print(employee)
#6
employee = ["Aswini", 10, 10.5, 10 + 5j]
employee.remove("Aswini") #removes the specified value
print(employee)
#7
employee = ["Aswini", 10, 10.5, 10 + 5j]
employee.pop(2)#removes the specified position value
print(employee)
#8
employee = ["Aswini", 10, 10.5, 10 + 5j]
employee.copy() #copies the list 
print(employee)
#9
employee = ["Aswini", 10, 10.5, 10 + 5j]
a = employee.index(10)
print(a)

#sort methods where it arranges an elements of an existing element in ascending or descending order
employee = [10, 30, 20, 50, 60, 70]
employee.sort()
print(employee) 
#reverse true for descending order
employee = [30, 20, 80, 40, 50, 10]
employee.sort(reverse=True)
print(employee) 

#can change the index
employee = ["aswini", "subhadra", "navya"]
employee[1] = "nagamani"
print(employee)

#nested lists means list inside the lists
employee = [
    ["aswini", 40],
    ["likky", 50],
    ["teju", 60]
]

print(employee)

#can access nested list with index
employee = [
    ["aswini", 40],
    ["likky", 50],
    ["teju", 60]
]
print(employee[0])
print(employee[0][1])
print(employee)

#modifying nested lists
employee = [
    ["aswini", 40],
    ["likky", 50],
    ["teju", 60]
]
employee[0][1] = 70
print(employee)

#creation of sets
numbers = {10, 40, 50, 10, 30, 60} #it dont allow duplicate values
print(numbers)
print(type(numbers))

#different ways to create a set 
#using {}
aswini = {"apple", "banana", "guava"}
print (aswini)
print(type(aswini))

#using set() constructor
aswini = set(["aswini", "apple", "banana"])
print(aswini)
print(type(aswini))

#creating an empty set
aswini = set()
print(aswini)
print(type(aswini))  #if we dont dont use set() here it gives us a dict type

#sets automatically removes duplicate values
aswini = {10, 20, 30, 40, 30, 20, 20, 60}
print(aswini)
print(type(aswini))

#set methods 
#add adds one element to the set
aswini = {"apple", "blueberry", "mango"}
aswini.add("guavava")
print(aswini)

#update adds more element to the set
aswini = {"apple", "blueberry", "mango"}
aswini.update(["guavava", "kiwi", "strawberry"])
print(aswini)

#remove removes the element from the set if the element is not present it gives an error
aswini = {"apple", "blueberry", "mango"}
aswini.remove("apple")
print(aswini)

# aswini = {"apple", "blueberry", "mango"}
# aswini.remove("guava")
# print(aswini)

#discard removes the lement if it is not present also it doesnot sends an error
aswini = {"apple", "blueberry", "mango"}
aswini.discard("guava")
print(aswini)

#copy creates a shallow copy
aswini = {"apple", "blueberry", "mango"}
aswini.copy()
print(aswini)

#clear removes the all sets
aswini = {"apple", "blueberry", "mango"}
aswini.clear()
print(aswini)

#pop removes and returns an arbitary element from set
aswini = {10, 20, 30, 40}
b = aswini.pop()
print("removed:", b)
print(aswini)

#set operations - union it combines all unique elements from both the sets without duplicates
aswini = {"apple", "banana", "mango"}
python = {"guava", "banana", "python"}
result = aswini.union(python)
print(result)

#intersection returns common values from both sets
aswini = {"apple", "banana", "mango"}
python = {"guava", "banana", "python"}
result = aswini.intersection(python)
print(result)
#difference returns the elements from set a not in set b it removes duplicate values
aswini = {"apple", "banana", "mango"}
python = {"guava", "banana", "python"}
result = aswini.difference(python)
print(result)
#symmetric_difference gives non common elements either sets removes common 
aswini = {"apple", "banana", "mango"}
python = {"guava", "banana", "python"}
result = aswini.symmetric_difference(python)
print(result)
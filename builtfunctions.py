#length it returns the length of the element
numbers = (10, 20, 30, 40, 50)
print(len(numbers))
#sum it returns the total of number elememnt
numbers = (10, 20, 30, 40, 50)
print(sum(numbers))
#max it returns the max value of the element
numbers = (10,30, 50, 70, 100)
print(max(numbers))
#max with strings
fruits = "apple", "banana", "guavava", "elephant"
print(max(fruits))
#min returns the max value of the element
numbers = (10,30, 50, 70, 100)
print(min(numbers))
#min with strings
fruits = "apple", "banana", "guavava", "elephant"
print(min(fruits))
#sorted this function returns a new sorted list ascending and descending
numbers = (50, 40, 20, 10, 70, 80)
print(sorted(numbers))
#descending order
numbers = (50, 40, 20, 10, 70, 80)
print(sorted(numbers, reverse=True))
#any returns true if any one elemnt is true returns false if all elements are false
numbers = [0,0,1]
print(any(numbers))
numbers = [0,0,0]
print(any(numbers)) #returns false bcoz all bacame false
#all returns true if all elemts are true returns false if any one element is false
numbers = [0,0,0]
print(all(numbers))
numbers = [1,0,0]
print(all(numbers))
numbers = [1,1,1]
print(all(numbers))
#zip combines multiple iterable element by element
numbers = [10, 20, 30, 40, 50]
names = ["Aswini", "likky", "teju"]
result = zip(numbers,names)
print(list(result))
#enumerate adds an index number to each element
a = ["Python", "Java", "C++"]
for i, v in enumerate(a):
    print(i, v)
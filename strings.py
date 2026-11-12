#string creation
python = "apple"
city = "hyderabad"
message = "welcome to learning path"
print(python)
print(city)
print(message)
#string methods
language = "python programming"
print(language.upper())
print(language.lower())
print(language.replace("python", "c"))
print(language.count("thon"))
print(language.index("p"))
print(language.startswith("pro"))
print(language.endswith("pyt"))
print(language.title())
print(language.capitalize())

#strings indexing
employee = "aswini"
print(employee[3])
print(employee[-1])
print(employee[-2])
print(employee[-3])
employee = "aswini", "letitbe", "subhadra" #negative indexing
print(employee[2])
print(employee[-1])
print(employee[-2])
print(employee[-3])
#string slicing means accessing some portions
is_learning = "python"
print(is_learning[0:2]) #wont access 2nd index the o/p will be py
print(is_learning[0:6])
print(is_learning[:])
print(is_learning[0:])
print(is_learning[:2])
print(is_learning[-4:-1])
print(is_learning[:])
print(is_learning[-1:])
print(is_learning[:-4])
print(is_learning[-3:-2])

#string ,manipulation is the process of performing different operations like modifying extracting combing on the strings
#concatenation
first_name = "aswini"
last_name = "padileti"
result = first_name + last_name
print(result)

#if we want space
first_name = "aswini"
last_name = "padileti"
result = first_name + " " + last_name
print(result)

#repetition
fruits = "apple"
print (fruits * 3)

#membership operator we use in and not in to check substring is existing or not
language = "python programming"
print("python" in language)
print("java" in language)
print("java" not in language)

#finding the string length
text = "hello python"
print (len(text))

#removing spaces
text = "     hello world    "
result = text.strip()
print(result)

#replacing characters
fruits = "banana"
result = fruits.replace("a", "@")
print(result)

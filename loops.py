#for loop iterates ob=ver a sequence (list, tuples, strings ,range)
for i in range(1,6):  #range
    print(i)

#for in list 
a = [10, 20, 30]
for i in a:
    print(i)

#for in strings
a = "Aswini"
for i in a:
    print(i)

#for in tuples
a = ("aswini", 10,20, 30)
for i in a:
    print(i)

#while lopp executes the code as long as the condition is satisfies
i = 1
while i <= 5:
    print(i)
    i += 1

#what happens when we dont write i+=1 itnever changes the condition
# i = 1
# while i <= 5:
#     print(i)

#continue statemnt skips the current iteration and move to the next one
for i in 'Aswini':
    if i == 's' or i == 'i':
        continue
    print(i)

#range in continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#break statement immediately breaks when the condition is met
for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in 'Aswini':
    if i == 's' or i == 'i':
       break
    print(i)

#pass statemnt when no needs to be executed
for i in 'aswini':
    pass
print("hello")

#range 1 argument
for i in range(4):
    print(i)

#2 argumenrt
for i in range(1,10):
    print(i)
#3 arguments range included step
for i in range(1,10,3):
    print(i)

#break in range
for i in range(2,7):
    if i == 5:
        break
    print(i)

#continue in range
for i in range(2,7):
    if i == 4 and i == 3:
        continue
    print(i)

#loop else
for i in range(1,7):
    print(i)
else:
    print("successfully executed")

#break
for i in range(1,10):
    if i == 3:
        break
    print(i)
else:
    print("wont execute")

    

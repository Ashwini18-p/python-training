#recursion is the process where the function itself calls the function itsef until it satisfies the condition
#base condition which stops the condition after the function gets satisfied so that python wont raise recursiveeroor
def count(n):
    if n == 5:   #base condition 
        return 
    print(n)
    count(n + 1)
count(1)

#without base condition recursion raises the error
# def show():
#     print("Hello")
#     show()

# show()

def count(n):
    if n == 1:   
        return 
    print(n)
    count(n - 1)
count(5)

def count(n):
    if n == 5:   #base condition 
        return 
    print(n * 2)
    count(n + 1)
count(1)

#print numbers from 1 to 10 
def numbers(n):
    if n > 10:
        return
    print(n)
    numbers(n + 1)
numbers(1)

# to print the numbers from 10 to 1
def numbers(n):
    if n == 0:
        return
    print(n)
    numbers(n - 1)
numbers(10)

#to print numbers from 5 to 15
def numbers(n):
    if n > 15:
        return
    print(n)
    numbers(n + 1)
numbers(5)

#to print numbers from 15 to 5
def numbers(n):
    if n < 5:
        return
    print(n)
    numbers(n - 1)
numbers(15)



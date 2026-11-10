#creationn of tuple
#giving only one character
busy = (10,) # we use comma here bcoz when we print type we will get int
print(busy)
print(type(busy))

busy = (10, "aswini", 20.5)
print(busy)
print(type(busy))

#indexing in tuples
busy = ("ASwini", "aswini", 10, 20, 30, 40)
print(busy[1])
print(busy[5])
print(busy[-1])
print(busy[-3])

#slicing in tuples
busy = ("ASwini", "aswini", 10, 20, 30, 40)
print(busy[0:3])
print(busy[0:])
print(busy[:3])
print(busy[:])
print(busy[0:6])
print(busy[-3:-1])
print(busy[-4:-2])

#packing the tuples
triangle = "rectangle","circle", 4 , 10.2
print(triangle)

#unpacking the tuples
busy = ( 10, 20, 30, 40)
a, b, c, d = busy
print(a,b,c,d)
print(a)
print(b)
print(c)
print(d)

#unpacking using * operator it takes remaining all the values in the tuple
busy = ( 10, 20, 30, 40)
*a, b, c = busy
print(a,b,c)

#tuple immutability tuples are ordered and immutable so that we cant change the value after execution insted we can create a  new tuple
immutability = (10,20,30)
immutue = immutability + (40,50,60)
print(immutability)
print(immutue)
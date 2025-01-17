#example1 chang from one type to another
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#example2 random
import random

print(random.randrange(1, 10))

#example3 integers
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#example4 floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#example5 strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#example6 Get the character at position 1
a = "Hello, World!"
print(a[1])

#example7
for x in "banana":
  print(x)


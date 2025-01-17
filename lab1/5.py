#example1 legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#example2 multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#example3 unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#example4 function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#example5 global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

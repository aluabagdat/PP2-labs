#Write a Python program that invoke square root function after specific milliseconds.
import time
import math

a = int(input())
b = int(input())

time.sleep(b/1000)
print("Square root of", a, "after", b, "miliseconds is", math.sqrt(a))

#sample output: Square root of 25100 after 2123 miliseconds is 158.42979517754858
"""
You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of 
numbers as an agrument and returns only prime numbers from the list.
"""

def filter_prime(numbers):
    listt= []
    for i in numbers:
        cnt = 0
        if (i == 2):
            listt.append(i)
            continue
        elif(i == 1):
            continue
        for j in range(2, i):
            if(i % j == 0):
                cnt += 1
        if(cnt == 0):
            listt.append(i)
    return listt

print(filter_prime([2,6, 7, 9]))

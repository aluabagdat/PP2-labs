"""
Define a functino histogram() that takes a list of 
integers and prints a histogram to the screen.
"""
def histogram(nums):
    for i in nums:
        for j  in range(i):
            print("*", end = "")
        print()
     
histogram([4, 6 ,7]) 
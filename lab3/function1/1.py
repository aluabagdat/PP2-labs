"""
A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. 
Create a function to convert grams to ounces. ounces = 28.3495231 * grams
"""

gr = float(input())
def convert(gr):
    return gr * 28.3495231

print(convert(gr))

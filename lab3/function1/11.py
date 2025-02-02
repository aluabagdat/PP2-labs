#Write a Python function that checks whether a word or phrase is palindrome or not.

s = str(input())

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(palindrome(s))

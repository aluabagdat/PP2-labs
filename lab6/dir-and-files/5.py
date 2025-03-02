#Write a Python program to write a list to a file.

items = ["there", "should", "be", "text", "there"]
file = open('filee.txt','w')
for item in items:
	file.write(item+"\n")
file.close()
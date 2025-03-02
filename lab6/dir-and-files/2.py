#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability and executability of the specified path

import os

print('Exist:', os.access('C://Users//admin//OneDrive//Рабочий стол//pp2', os.F_OK))
print('Readable:', os.access('C://Users//admin//OneDrive//Рабочий стол//pp2', os.R_OK))
print('Writable:', os.access('C://Users//admin//OneDrive//Рабочий стол//pp2', os.W_OK))
print('Executable:', os.access('C://Users//admin//OneDrive//Рабочий стол//pp2', os.X_OK))
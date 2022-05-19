#Handling Creating Writing to a File

#Files
"""
>Files - are the named locations where you securely store your data 
Types of Files
1. Binary Files - are used for storing media files, compiled code, or app data.
2. Text Files - are readable to use (plain text, source code)
"""

#Functions used for files 
"""
>open() function parameters
open() function has two parameters: 
    open(filename, mode)

>How do we open a file?
r(read), a(append), w(write), x(create)

f = open("newfile.txt", "x") #x used to create new files

====
f = open("newfile.txt", "w") #w opens the files for us to write. Also overwwrite existing content
f.write("Python is easy!") #It can also be used to create new files. 

f = open("newfile.txt", "r") 
print(f.read())
f.close()

====
f= open("newfile.txt", "a") #a appends, or adds, to something. It can also used to create a new file

f.write("Python Intermediate")

f = open("newfile.txt", "r") 
print(f.read())
f.close()

"""

#Reading from a file
"""
r(read) - default value for python 
FileNotFoundError - if the file doesn't exist

f = open("newfile.txt", "rt") #access file 
or
f = open("newfile.txt")

#example
f = open("newfile.txt", "r") #file is an object
print(f.read()) #file more 'r' return the whole text.
"""

#Reading specific parts of a files
"""
f = open("newfile.txt", "r")
print(f.read(12))

>readline() - returns a single line
f = open("newfile.txt", "r")
print(f.readline())

>for loops - allows to read the whole file one line at a time
for x in f:
    print(x)

>always close the files
f.close()
"""

#Deleting a file
"""
>if not sure if the file exist
import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("The files doesn't exists")

>if sure the file exists
import os
os.remove("newfile.txt")
"""
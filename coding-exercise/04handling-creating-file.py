
f = open("testing.txt", "w")
f.write("Python is easy.")

f = open("testing.txt", "a")
f.write("\nBackend")
f.write("\nDo projects")
f.write("\nMaster python")

f = open("testing.txt", "r") 
f.close()

#Reading File
f = open("testing.txt", "r")
print(f.read()) 
"""
Output: 
Python is easy.
Backend
Do projects
Master python
"""

f = open("testing.txt", "r")
print(f.readline()) #Output: Python is easy.

f = open("testing.txt", "r")
for x in f:
    print(x)
"""
Output: 
Python is easy.

Backend

Do projects

Master python
"""

#Deleting a file
import os
if os.path.exists("testing.txt"):
    os.remove("testing.txt")
else:
    print("File does not exist")
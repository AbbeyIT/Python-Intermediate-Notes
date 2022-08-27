# Handling Creating Writing to a File 

## Files
**Files** are the named locations where you securely store your data 

**Types of Files**
1. Binary Files - are used for storing media files, compiled code, or app data.
2. Text Files - are readable to use (plain text, source code)


## Functions used for files 
**open() function parameters**
```
open() function has two parameters: 
    open(filename, mode)
```

## How do we open a file?
> r(read), a(append), w(write), x(create)
```
f = open("newfile.txt", "x") #x used to create new files
```
```
f = open("newfile.txt", "w") #w opens the files for us to write. Also overwwrite existing content
f.write("Python is easy!") #It can also be used to create new files. 
```
```
f = open("newfile.txt", "r") 
print(f.read())
f.close()
```
```
f= open("newfile.txt", "a") #a appends, or adds, to something. It can also used to create a new file

f.write("Python Intermediate")

f = open("newfile.txt", "r") 
print(f.read())
f.close()
```

# Reading from a file

**r(read)** - default value for python 
**FileNotFoundError** - if the file doesn't exist
```
f = open("newfile.txt", "rt") #access file
```
or
```
f = open("newfile.txt")
```

### Example
```
f = open("newfile.txt", "r") #file is an object
print(f.read()) #file more 'r' return the whole text.
```

## Reading specific parts of a files
```
f = open("newfile.txt", "r")
print(f.read(12))
```
**readline()** - returns a single line
```
f = open("newfile.txt", "r")
print(f.readline())
```

**for loops** - allows to read the whole file one line at a time
```
for x in f:
    print(x)
```
**always close the files**
```
f.close()
```

## Deleting a file
### if not sure if the file exist
```
import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("The files doesn't exists")
```
### if sure the file exists
```
import os
os.remove("newfile.txt")
```

# Exceptions 
**Exception** - is an object which tell you about the problem you encountered. It also provibes a traceback, which tells
you specifically where you made a blunder in your code. 

## Built-in excetions
1. raise keywoard - lets us throw an excetion. We can use it to define the error we'd like to raise, and what text
will be printed on the console

>Example: we dont want any negative values
```
n = -5
if n < 0:
    raise Exception("No negative numbers allowed")
```

2. syntax error - occurs when the code is not written correctly

3. assertions - boolean expressions that make sure that the conditions are true.

> Example: 
```
employee_of_the_year = "Roger"

assert employee_of_the_year == "Roger"
#can also be used for debugging tool because its stops the program as soon as an error occur
assert employee_of_the_year == "Shane" #error because we also assign shane as employee of the year
```

4. ZeroDivisionError - occurs when you divide by zero

> Example: 
```
1/0
```

5. TypeError - occurs when an operation is performed on an incorrect or unsupported object type. 

> Example: 
```
50 ** "two"
```

## How we can handle them? 
**try except** - these blocks are used to spot and handle exceptions

**try** - test the code to ensure that there are no errors

**except** - if we don't handle an exception with an except block, the program will crash

**finally** - finally block allows us to run our code no matter what the result of the try and except blocks is

Example: 
```
try: 
    print(random_var)
except:
    print("Exception Alert!")
```
```
try:
    print(x + "macarons")
except NameError:
    print("Please define your variable")
except IndentationError:
    print("Please be careful with your identing your code.")
except:
    print("Something else went wrong. We need to figure it out.")
```
```
try:
    print(24 + 42)
except:
    print("This operation cannot be performed")
else:
    print("No issues here!")
```
```
try: 
    print(n)
except:
    print("There something wrong with our program.")
finally:
    print("Let's run our program anyway") #run our code even there's error
```

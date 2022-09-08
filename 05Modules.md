# Modules 
**Modules** - is a Python object containing many different attributes. There are many different kind of modules, each with Python codes that we can reuse.

## Advantage of module 
- When you divide your code into modules, it will be easier to reuse, since they are already categorized.
- Modules can minimize our lines of code

## import keywoard is used to import modules

> How to create a module : open() function(thorugh a calculator) -
*main.py*
f = open("module.py", "x) #same as files, but file name saved as .py

*module.py*
def greeting(name):
    print("Hey there, " + name + "! Ready to do some math?")

*main.py*
import module 

module.greeting("Jolina") #Output Hey there, Jolina! Ready to do some math?

- Using a class -
*module.py*
class User:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

user_1 = User("Jolina", 23, "Philippines")
user_2 = User("Fifi", 21, "Japan")
user_3 = User("Mika", 25, "Australia")

*main.py*
import module

a = module.user_1
print("Hey there, " + a.name + "! Ready to do some math?") #Output: Hey there, Jolina! Ready to do some math?

c = module.user_3
print("Hey there, " + c.name + "! Ready to do some math?") #Output: Hey there, Mika! Ready to do some math?


- Renaming modules -
>>You can create an alias when you import a module. This can be done using "as" keyword.

*main.py*
import module as mod

c = mod.user_3
print("Hey there, " + c.name + "! Ready to do some math?") #Output: Hey there, Mika! Ready to do some math?

- Other Functions (mathematical) -
*module.py*
def get_sum(x, y):
    return x + y

def get_diff(x, y):
    return x - y

def get_prod(x, y):
    return x * y

def get_quo(x, y):
    return x / y

*main.py*
import module 

sum = module.get_sum(12, 45)
print(sum) #Output: 57

>>return statement - sends the function's results back to the caller

- Importing modules -
>>The from keyword can also be used to import modules. 

*main.py*
from module import * #to get all the data from the module

product = get_prod(3, 5)
print(product) #Output: 15

Note: The from keywoard can be used to import a single function from a module
from module import get_quo
"""


# === Built-In Python Modules ===#
"""
help("modules") function - to see a comprehensive list of all built-in modules in python
help("random") - to view all the attributes you want to import, type the module name inside the ()
print(dir("random")) 
dir - returns a list of valid attributes of the object

===
random module - is a module that provides pseuso-random numbers 
randint() function - is the function used to provide random numbers
Example: There's a raffle and there are many prizes. My friend Jolina got ticket number 8 out of 1000 tickets. 
She has her eyes on those mechanical keyboard. Let's see if she'll get lucky.

from random import randint 
print(int(randint(1,1000)))

===
Datetime module - provides class which allow us to work with date and time 

import datetime
t = datetime.datetime.now()
print(t)

===
strftime() method - which will make strings out of our imported date objects. 

import datetime 

t = datetime.datetime(2022, 06, 08)
print(t.strftime("%B"))
print(t.year)

x = datetime.datetime(1963, 8, 28))
print(x)
"""


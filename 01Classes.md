# Object-Oriented Programming

**OOP** is a method or approach of organizing a program by grouping properties, methods and attributes into 
indivisual objects
```
class Guest:
    def __init__(self, first, last,):
        self.first = first
        self.last = last

g1 = Guest("Adam", "DC")
g2 = Guest("Eve", "AV")

print(g1.first)
print(g1.last)
```

## Class
**Class** is the blueprint or template for creating instance and objects; helps us organize our data and functions
so that they can be reused or modified if necessary
```
class NewClass:
    pass
```

## Pass
**Pass** is a temporary placeholder for future code, which is used to prevent Identation Error


## Objects
**Objects** are data structures that are defined by its class, comprised of methods, class variables, 
and instance variables.
```
class Guest:
    def __init__(self, first, last,):
        self.first = first
        self.last = last

g1 = Guest("Adam", "DC")
g2 = Guest("Eve", "AV")

print(g1.first)
print(g1.last)
```

## Attributes
**Attributes** are data stored inside a class or instance that represents the state of the class or instance
```
class GuessA:
    pass
g_1 = "roar"
g_1.first = "Haha" #Attributes
```

## Methods 
**Methods** are a type of function that is defined in a class
```
class Guest:
    def __init__(self, first, last,): #Methods
        self.first = first
        self.last = last

g1 = Guest("Adam", "DC")
g2 = Guest("Eve", "AV")

print(g1.first)
print(g1.last)
```

## Class Variables
**Class Variables** are variables that are used by all instances of the class, which can be defined within a class,
but not within the method of the class
```
class Pets:
    looks = "Adorable" #Class Variables
hamster = Pets()
print(hamster.looks)
```

## Instance Variables 
**Instance Variables** are variables that are defined within a method and are unique to a certain instance
```
class Honey:
    pass
p1 = Honey()
p1.first = "Sweet"  #Instance Variables
```

## ___init___ method
___init___ method is used to assign values to the properties and operations of object when it is being created

#Animals

class Horse(): 
     def type(self): 
       print("Mammal") 
     def name(self):
       print("Mal") 
class Turtle(): 
     def type(self): 
       print("Reptile") 
     def name(self): 
       print("Totul")
class Frog(): 
     def type(self): 
       print("Amphibian") 
     def name(self): 
       print("Keguri")
class Eagle(): 
     def type(self): 
       print("Bird") 
     def name(self): 
       print("Doksu")
class Salmon(): 
     def type(self): 
       print("Fish") 
     def name(self): 
       print("Yon") 
      
#Initializing the class
def func(obj): 
       obj.type() 
       obj.name()

#Calling the class
obj_Horse = Horse() 
obj_Turtle = Turtle()
obj_Frog = Frog()
obj_Eagle = Eagle()
obj_Salmon = Salmon() 
func(obj_Horse) 
func(obj_Turtle)
func(obj_Frog)
func(obj_Eagle)
func(obj_Salmon)

#Another way to call the class
# Attributes having same name are considered as duck typing
print("")
print("Animal Type")
for obj in Horse(), Turtle(), Frog(), Eagle(), Salmon() :
    obj.type()

print("")
print("Animal name")
for obj in Horse(), Turtle(), Frog(), Eagle(), Salmon() :
    obj.name()

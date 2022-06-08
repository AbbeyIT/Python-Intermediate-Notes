#raise an exception
x = 500
if x > 100:
    raise Exception("Error will show if x is bigger than 100")

#undefined var 
try:
    print(variable_1)
except:
    print("variable_1 is not defined")

for i in range(6):
    print("I am so happy!")

#using conditional statement
try:
    print(12*6)
except:
    print("This operation cannot be performed")
else:
    print("No issues here!")

#assertion error
best_burger = "burger king"
number_2_burger = "mcdonalds"

assert best_burger == "burger king"
assert best_burger == "mcdonalds"
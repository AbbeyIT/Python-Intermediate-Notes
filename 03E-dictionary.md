## Dictionary
**Dictionary** is a collection of unordered data, which is stored in key-value pairs.
```
price_list = {
    "jeans": 134,
    "shirt": 135, 
    "shoes": 153,
}
```

## Key-Value pairs
A **key-value pair** is a set of values associated with each other. 
```
price_list = {
    "jeans": 134, #key-value pair
    "shirt": 135, 
    "shoes": 153,
}
```

### Key
**Key** is a unique identifier for some item in the data.
```
price_list = {
    "jeans": #Key
}
```

## Value
The **value** is that data that is identified or a pointer to the location of the data.
```
price_list = {
    "jeans": 425 #value - 425
}
```

## .update() method
The **update method** updates dictionary with the specifies key and value pairs.
```
price_list.update =  ({
    "boots": 563,
    "sneakers": 326 })
```

## zip() function
The **zip function** is used to quickly combine associated data-sets without needing to rely on multi-dimensional lists.
```
var1 = ["weight", "height"]
var2 = [35, 536]
combined_variables = zip(var1, var2)
```

## dict function
The **dict function** turns the combined list into a dictionary
```
relative = ["a", "b", "c"]
num = [1, 2, 3]
dictVar = dict(zip(relative, num))
print(dictVar)
```

# Navigating in dictionary

## Getting a key from the dictionary
```
test_scores = {"jonathan": 64, "abra": 98, "key": 86, "jane": 36}
print(test_scores["jane"])
```

**KeyError** occurs when you input a key that isn't present in the dictionary/code

## Checking if the key is present
```
check_Key = "andrew"

if check_Key in text_scores:
    print(check_Key, "took the test")
else:
    print(check_Key, "didn't took the test")
```

## .get()method
The **.get()method** shows us the key we're looking for. If it doesn't exist, it return none.
```
print(test_scores.get("abra"))
print(test_scores.get("cong")) #print "None" if it doesn't exist
```

## .pop()method
If you want to delete a key in the dictionary/code
```
neighbors = {"Ms. Santos": "fruitcake", "Toni": "socks", "Alex": "vinegar"}
print(neighbors)
```

## .keys()method
If you want to get all the keys without their values 
```
neighbors = {"Ms. Santos": "fruitcake", "Toni": "socks", "Alex": "vinegar"}
done = neighbors.pop("Ms. Santos")
y = neighbors.keys()
print(y)
```

## .values()method
To get all the values without their keys
```
neighbors = {"Ms. Santos": "fruitcake", "Toni": "socks", "Alex": "vinegar"}
done = neighbors.pop("Ms. Santos")
w = neighbors.values()
print(w)
```
## .items()method
Shows both keys and values 
```
neighbors = {"Ms. Santos": "fruitcake", "Toni": "socks", "Alex": "vinegar"}
done = neighbors.pop("Ms. Santos")
z = neighbors.items()
print(z)
```


# Looping Through Dictionaries
```
neighbors = {"Ms. Santos": "fruitcake", "Toni": "socks", "Alex": "vinegar"}
```

## using .items()
```
for key, value in neighbors.items():
    print(key)
    print(value)
```

## using .keys()
```
for name in neighbors.keys():
    print(name)
```    

## continue
```
for name in neighbors.keys():
    if name == "Ms. Santos":
        continue
    print(name)
```    
## .values()
```
for gift in neighbors.values():
    print(gift)
```

## nested keyword (dictionary within a dictionary)
```
cat = { 1: {"name": "pepper", "age": 5, "color": "black"}, 
        2: {"name": "sashimi", "age": 6, "color": "gray"} }
```
## [] to access elements of each dictionaries
```
print(cat[2]["age"])
print(cat[1]["color"])
```

## {} create a new dictionary
```
cat[3] = {}
cat[3]["name"] = "tuna"
cat[3]["age"] = 2
cat[3]["color"] = "orange"
cat[3]["personality"] = "wild"
print(cat[3])
print(cat[3]["personality"])
print(cat[1])
```
## another method to add a dictionary
```
cat[4] = {"name": "sushi", "age": 10, "color": "white", "personality": "shy"}
print(cat[3])
print(cat[4])
print(cat[4]["age"])
```


#.pop()method
groceries = {"chicken": 8, "apples": 6, "cucumbers": 3, "milk": 2, "oranges": 4}
done = groceries.pop("chicken")
print(groceries)


#.keys()method
speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}
name = speakers.keys()
print(name)


#.get()method
swimming_team = {"Carl": "passed", "Quentin": "failed", "John Y.": "passed", "Peter": "failed", "Max T.": "passed", "Joseph": "passed", 
" Jone": "failed", "Jorge": "failed", "George": "passed", "Ben": "passed", "Jerome": "passed", "Rick": "failed", "Max G.": "failed", 
"John P.": "failed", "Vince": "passed"}
find = swimming_team.get("Jorge")
print(find) #print(swimming_team.get("Jorge"))
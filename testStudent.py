names = [] # creates empty list called names
doneEntering = False
while (not doneEntering):
    name = input("Enter a name, or leave blank when done: ")
    name = name.strip()
    if (name == ""):
        doneEntering = True
    else:
        names.append(name)
print(names)
import os
path = input("Enter your Directory path: ")
path = os.chdir(path)
name = input("Would your start file name with what Name? ")
type = input("Whats Format of these Files: ")
number = int(input("Start file index: ").strip() or "1")

for theFile in os.listdir(path):

    theNumber = "{:02d}".format(number)
    newCompeleteName = f"{name}_{theNumber}.{type}"
    os.rename(theFile, newCompeleteName)
    number += 1

print("All Done!")
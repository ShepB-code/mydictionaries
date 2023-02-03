# Author:     Shepard Berry
# Class:      MIS-4322
# Due:        2/8/2023
# Assignment: Dictionaries

person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}


print(person)

# The name of the second child

print(person["children"][1])

# The name of the cat

print(person["pets"]["cat"])

# Loop to list each child

for c in person["children"]:
    print(c)

# print out the pets in this format (type:name)

for k, v in person["pets"].items():
    print(f'Tyep of pet:{k} Name of pet:{v}')
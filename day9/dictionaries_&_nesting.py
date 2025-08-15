# dictionary

details = {
    "name" : "nagur diwakar",
    "city" : "tirupati",
    "role" : "devops Engineer"
}

print(details["name"])

# to add the data into the dictionary

details["company"] = "expedia"

print(details)

# empty dictionary

empty_dictionary = {}

print(empty_dictionary)

#wipe or delete or clean existing dictionary
# down below i am just adding existing data with in the dictinary declare it as empty

#details = {}

print(details)

#edit an item in the dictionary ... or replacing existing dictionary
# i am just changing the value with new value

details["name"] = "gayathri"

# loop through dictionary
# it only loop through the key one after the other
# to print all the values with key
for i in details:
    print(i)
    print(details[i])
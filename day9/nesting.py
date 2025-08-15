# dictionaries contains dictionaries nested dictionary

# instead of just value for key we can use the list and dict as a value

#https://www.w3schools.com/python/python_dictionaries_nested.asp

dictionary = {
    "key" : [list],
    "keyone" : "value"
}

# nested list in a dictionary

travel_log = {
    "india" : ['andhra','telangana','tamilnadu']

}

# to print out only telangana from the above dictionary

print(travel_log["india"][1])

# to print the list with inside another list 

nested_list = ['a','b',['c','d']]

# list we want print is in second of the list

print(nested_list[2][1])

# list nested inside in a dictionary and nested in another dictionary

travel = {
    "countaries" : {
        "num_of_visitors" : 8,
        "cities_visited" : ["kochi","vijaywada","hyderabad"]

    },
    "india" : ['andhra','telangana','tamilnadu']

}


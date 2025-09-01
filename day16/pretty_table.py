from prettytable import PrettyTable

table = PrettyTable()

# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

table.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])

# we can also change the attributes

table.align = "l"

print(table)
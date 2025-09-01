MenuItem Class
Attributes:
-
name
(str) The name of the drink.
e.g.
“latte”
-
cost
(float) The price of the drink.
e.g 1.5
-
ingredients
(dictionary) The ingredients and amounts required to make the drink.
e.g. {“water”: 100,
“coffee”: 16}
Menu Class
Methods:
-
get
items()
_
Returns all the names of the available menu items as a concatenated string.
e.g.
“latte/espresso/cappuccino”
-
find
drink(order
name)
_
_
Parameter order
name: (str) The name of the drinks order.
_
Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
otherwise returns None.
CoffeeMaker Class
Methods:
-
report()
Prints a report of all resources.
e.g.
Water: 300ml
Milk: 200ml
Coffee: 100g
-
is
resource
sufficient(drink)
_
_
Parameter drink: (MenuItem) The MenuItem object to make.
Prints a message if ingredients are insufficient.
Returns True when the drink order can be made, e.g.
True
False if ingredients are insufficient.
-
make
coffee(order)
_
Parameter order: (MenuItem) The MenuItem object to make.
Deducts the required ingredients from the resources.
MoneyMachine Class
Methods:
-
report()
Prints the current profit
e.g.
Money: $0
-
make
_payment(cost)
Parameter cost: (float) The cost of the drink.
Returns True when payment is accepted, or False if insufficient.
e.g. False
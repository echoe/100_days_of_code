from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
"""
This needs the Menu, MenuItem, CoffeeMaker, and MoneyMachine modules
from this class to run properly.
Mostly I'm saving this to the git repo so I can save the study results today:
-I used print() around the report functionality, which was incorrect.
-I did not grab the options from the menu initially.
-I added an else that was not necessary.
I think the documentation for this was a bit rough, but it worked in the end!
Also set up my anaconda environment properly today, and got Git working within
my IDE of choice (VSCode, not PyCharm). That was nice.
"""

is_on = True
coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    options = coffee_menu.get_items()
    drink_selection = input(f"What would you like? ({options}):").lower()
    if drink_selection == "off":
        is_on = False
    elif drink_selection == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        menu_drink = coffee_menu.find_drink(drink_selection)
        if coffee_maker.is_resource_sufficient(menu_drink):
            if money_machine.make_payment(menu_drink.cost):
                coffee_maker.make_coffee(menu_drink)
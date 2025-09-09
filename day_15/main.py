"""
A coffee machine! Wowee
"""

# Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# Check user's input to decide what to do next
# TODO: The prompt should show every time action has completed (eg when the drink is dispensed)
# Turn off the Coffee Machine by entering "off" into the prompt.
# Print report.
# Check resources sufficient?
# Make coffee. The ingredients should change.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# Sets money so we can add and subtract money later.
money = 0.00

def check_resource(resource):
    """Checks to see if we can make the selected coffee with the resources we have in hand."""
    the_resource = MENU[resource]
    can_make = True
    if resources["water"] < the_resource["ingredients"]["water"]:
        print("Sorry, there is not enough water!")
        can_make = False
    try:
        if resources["milk"] < the_resource["ingredients"]["milk"]:
            print("Sorry, there is not enough milk!")
            can_make = False
    except KeyError:
        # This means that this drink is an espresso (has no milk) and we don't need to check it.
        pass
    if resources["coffee"] < the_resource["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee!")
        can_make = False
    return can_make

def print_resources():
    """Prints a report on the current usage of everything in the coffee machine."""
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: " + "$" + str(round(money, 2)))

def make_coffee(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

#Start the machine.
machine_on = True
while machine_on:
    drink_selection = input("What would you like? (espresso/latte/cappuccino):").lower()
    if drink_selection == "off":
        machine_on = False
    elif drink_selection == "report":
        print_resources()
    elif drink_selection in MENU:
        selection = MENU[drink_selection]
        if check_resource(drink_selection):
            quarters = input("How many quarters?: ")
            dimes = input("How many dimes?: ")
            nickels = input("How many nickels?: ")
            pennies = input("How many pennies?: ")
            total_coins = float(quarters) * 0.25 + float(dimes) * 0.1 + float(nickels) * .05 + float(pennies) * .01
            if selection["cost"] > total_coins:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                money += selection["cost"]
                make_coffee(drink_selection)
                if round(total_coins, 3) > round(selection["cost"], 3):
                    print(f"Here is ${round(total_coins - selection["cost"], 3)} in change.")
                print(f"Here is your {drink_selection}. Enjoy!")

    else:
        print("The drink selection you chose is not on the menu. Please order something on the menu.")
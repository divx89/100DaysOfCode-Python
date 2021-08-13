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

coinValue = {"quarter": 0.25,
             "dime": 0.1,
             "nickel": 0.05,
             "penny": 0.01}

choices_allowed = ("latte", "cappuccino", "espresso", "off", "report")


def total_amount_paid(coins):
    total = 0
    for type_of_coin in coins:
        num_coins = coins[type_of_coin]
        val_of_coin = coinValue[type_of_coin]
        total += num_coins * val_of_coin
    return total


def get_coins(drink):
    print(f"The cost of the drink is {MENU[drink]['cost']}")
    print("Please enter coins.")
    coins = {"quarter": float(input("How many Quarters? ")),
             "dime": float(input("How many Dimes? ")),
             "nickel": float(input("How many Nickels? ")),
             "penny": float(input("How many Pennies? "))}
    return coins


def modify_and_return_money(drink, amount):
    cost_of_drink = MENU[drink].get("cost", 0)
    resources["money"] = resources.get("money", 0) + cost_of_drink
    if amount > cost_of_drink:
        print(f"Here is ${round(amount - cost_of_drink, 2)} in change.")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    if "money" in resources:
        print(f"Money: ${resources['money']}")


def resources_available(drink):
    available = True

    water_needed = MENU[drink]["ingredients"].get("water", 0)
    coffee_needed = MENU[drink]["ingredients"].get("coffee", 0)
    milk_needed = MENU[drink]["ingredients"].get("milk", 0)

    insufficient = []
    if resources["milk"] < milk_needed:
        insufficient.append("milk")
    if resources["coffee"] < coffee_needed:
        insufficient.append("coffee")
    if resources["water"] < water_needed:
        insufficient.append("water")
    if len(insufficient) > 0:
        available = False
        print(f"Sorry, we don't have enough of {insufficient}")

    return available


def amount_sufficient(drink, amount):
    sufficient = True
    if amount < MENU[drink].get("cost", 0):
        sufficient = False
        print("Sorry, that's not enough money. Money refunded.")
    return sufficient


def make_and_serve(drink):
    resources["water"] -= MENU[drink]["ingredients"].get("water", 0)
    resources["coffee"] -= MENU[drink]["ingredients"].get("coffee", 0)
    resources["milk"] -= MENU[drink]["ingredients"].get("milk", 0)

    print(f"Here's your {drink} ☕. Enjoy!")


def get_choice():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice not in choices_allowed:
            print("Please enter one of the allowed choices only")
            print(choices_allowed)
        else:
            break
    return choice


def run_coffee_machine():
    shutdown_requested = False
    while not shutdown_requested:
        choice = get_choice()

        if choice == "off":
            shutdown_requested = True
            continue
        elif choice == "report":
            print_report()
            continue

        drink = choice
        if resources_available(drink):
            coins = get_coins(drink)
            amount = total_amount_paid(coins)
            if amount_sufficient(drink, amount):
                modify_and_return_money(drink, amount)
                make_and_serve(drink)


run_coffee_machine()
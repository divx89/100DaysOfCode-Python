from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_coffee_machine():
    coffee_menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    shutdown_requested = False

    while not shutdown_requested:
        choice = input(f"What would you like? ({coffee_menu.get_items()}): ")

        if choice == "off":
            shutdown_requested = True
            continue
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        drink = coffee_menu.find_drink(choice)

        if drink is not None and coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


run_coffee_machine()
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
pos_system = MoneyMachine()

next_drink = True
while next_drink:
    options = coffee_menu.get_items()
    selection = input(f"What would you like to drink? ({options}): ")
    if selection == "off":
        next_drink = False
    elif selection == "report":
        coffee_machine.report()
        pos_system.report()
    else:
        drink = coffee_menu.find_drink(selection)
        if coffee_machine.is_resource_sufficient(drink) and pos_system.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)



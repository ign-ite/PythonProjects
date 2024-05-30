from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()

menu = Menu()
menu_name = menu.get_items()


def main_program():
    userchoices = ""
    drink = ""
    while userchoices != "off":
        userchoices = input(f"What would you like to drink? ({menu_name}): ").lower()
        if userchoices == "off":
            print("Enjoy your day!")
            exit()
        elif userchoices == "report":
            coffee.report()
            money.report()
            main_program()
        else:
            drink = menu.find_drink(userchoices)
            if coffee.is_resource_sufficient(drink) is True:
                 if money.make_payment(drink.cost) is True:
                     coffee.make_coffee(drink)
            else:
                print("Sorry that's not enough money. Money refunded")

main_program()
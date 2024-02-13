# my code

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()


def running_machine(profit):
    while offer_coffe:
        answer = input(f"What would you like? ({menu.get_items()[0:-1]}): ")

        if answer == "report":
            coffee_maker.report()
            money.report()
            offering_coffe = True

        elif answer == "off":
            print("Coffee Machine turned off")
            offering_coffe = False

        elif menu.find_drink(answer):
            selected_drink = menu.find_drink(answer)
            drink_cost = selected_drink.cost
            if coffee_maker.is_resource_sufficient(selected_drink):
                coffee_maker.report()
                money.report()
                payment_successful = money.make_payment(drink_cost)
                if payment_successful:
                    coffee_maker.make_coffee(selected_drink)
                    coffee_maker.report()
                    money.report()
            offering_coffe = True
        else:
            offering_coffe = True

        return offering_coffe, profit


offer_coffe = True
while offer_coffe:
    run_machine = running_machine(0)
    offer_coffe = run_machine[0]
    start_profit = run_machine[1]

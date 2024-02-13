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

start_profit = 0

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 300,
}

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

# TODO:
"""Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2"""

# TODO: 3. Print report.
""" a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5"""


def reporting(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO:  4. Check resources sufficient?
"""a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee."""


def check_resources(drink):
    enough = True
    ingredients = []
    ingredients_str = ''

    water = resources['water'] - MENU[drink]["ingredients"]['water']
    coffee = resources['coffee'] - MENU[drink]["ingredients"]['coffee']
    try:
        milk = resources['milk'] - MENU[drink]["ingredients"]['milk']
    except:
        milk = 0

    if water < 0:
        ingredients.append('water')
        enough = False
    if coffee < 0:
        ingredients.append('coffee')
        enough = False
    if milk < 0:
        ingredients.append('milk')
        enough = False
    if water < 0 or coffee < 0 or milk < 0:
        for i in ingredients:
            ingredients_str += f'{i}, '
        print(f"Sorry there is not enough {ingredients_str[0:-2]}.")

    return enough


# TODO: 5. Process coins.
"""a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52"""

# TODO: 6. Check transaction successful?
"""a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places."""


def process_coins(drink):
    drink_price = MENU[drink]["cost"]
    entered_coins = 0
    print(f"Price: ${drink_price}")
    print("Please insert coins!")
    for coin_type in COINS:
        amount = int(input(f"How many {coin_type}?: "))
        entered_coins += (amount * COINS[coin_type])
        # print(f"Entered: ${entered_coins:.2f}")
    if drink_price > entered_coins:
        print(f"Price: ${drink_price}")
        print(f"Entered: ${entered_coins}")
        print("Sorry that's not enough money. Money refunded.")
        successful = False
    elif drink_price == entered_coins:

        successful = True
    elif drink_price < entered_coins:
        successful = True
        print(f"Here is ${round(entered_coins-drink_price, 2)} dollars in change.")
    else:
        successful = False
    return successful, drink_price


# TODO: 7. Make Coffee.
"""a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink."""


def make_drink(drink, money):
    money += MENU[drink]["cost"]
    print(f"Here is your {drink} Enjoy!")
    resources['water'] -= MENU[drink]["ingredients"]['water']
    resources['coffee'] -= MENU[drink]["ingredients"]['coffee']
    try:
        resources['milk'] -= MENU[drink]["ingredients"]['milk']
    except:
        pass

    return money, resources


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
"""a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer."""

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
"""a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens."""


def running_machine(profit):
    answer = input("What would you like? (espresso/latte/cappuccino): ")

    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        enough_resources = check_resources(answer)
        if enough_resources:
            if process_coins(answer)[0]:
                reporting(profit)
                result = make_drink(answer, profit)
                profit = result[0]
                reporting(profit)
        offering_coffe = True

    elif answer == "report":
        reporting(profit)
        offering_coffe = True

    elif answer == "off":
        print("Coffee Machine turned off")
        offering_coffe = False

    else:
        print("Wrong input!")
        offering_coffe = True
    return offering_coffe, profit


offer_coffe = True
while offer_coffe:
    run_machine = running_machine(start_profit)
    offer_coffe = run_machine[0]
    start_profit = run_machine[1]


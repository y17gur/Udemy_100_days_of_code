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


def reporting(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink):
    enough = True
    ingredients = []
    ingredients_str = ''

    water = resources['water'] - MENU[drink]["ingredients"]['water']
    coffee = resources['coffee'] - MENU[drink]["ingredients"]['coffee']
    try:
        milk = resources['milk'] - MENU[drink]["ingredients"]['milk']
    except KeyError:
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
        print(f"Here is ${round(entered_coins - drink_price, 2)} dollars in change.")
    else:
        successful = False
    return successful, drink_price


def make_drink(drink, money):
    money += MENU[drink]["cost"]
    print(f"Here is your {drink} Enjoy!")
    resources['water'] -= MENU[drink]["ingredients"]['water']
    resources['coffee'] -= MENU[drink]["ingredients"]['coffee']
    try:
        resources['milk'] -= MENU[drink]["ingredients"]['milk']
    except KeyError:
        pass

    return money, resources


def running_machine(profit):
    answer = input("What would you like? (espresso/latte/cappuccino): ")

    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        enough_resources = check_resources(answer)
        if enough_resources:
            reporting(profit)
            if process_coins(answer)[0]:
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

# Coffee Vending Machine.

# Program requirements:
# 1. Print report
# 2. Check resources sufficient?
# 3. Process coins.
# 4. Check transaction successful?
# 5. Make coffee.

import menu

profit = 0


def check_quantity(ingredients):
    """Return True when order can be satisfied or False if it cannot."""
    for item in ingredients:
        if ingredients[item] >= menu.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def check_coins():
    """Returns the total value of coins inserted"""
    print("Please insert coins: ")
    total = int(input("How many 1p?: ")) * 0.01
    total += int(input("How many 2p?: ")) * 0.02
    total += int(input("How many 5p?: ")) * 0.05
    total += int(input("How many 10p?: ")) * 0.10
    total += int(input("How many 20p?: ")) * 0.20
    total += int(input("How many 50p?: ")) * 0.50
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if inserted coins are sufficient to complete order or False if not."""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is £{change} in change.")
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts the drink ingredients from resources"""
    for item in order_ingredients:
        menu.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")


machine_on = True
while machine_on:

    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        machine_on = False
    elif order == "report":
        print(f"Water: {menu.resources['water']}ml")
        print(f"Milk: {menu.resources['milk']}ml")
        print(f"Coffee: {menu.resources['coffee']}g")
        print(f"Money: £{profit}")
    else:
        drink = menu.MENU[order]
        if check_quantity(drink["ingredients"]):
            payment = check_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])

# TODO 1: Prompt user for their drink option and decide what to do next, to maintain the coffee machine user can
#  enter "off"
from Coffee_Menu import resources, MENU

profit = 0


# TODO 3: Check resources sufficient
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO 4: Process coins
def process_coin():
    """ Return the total calculated  from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dime?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How  many pennies? ")) * 0.01
    return total


# TODO 5: Check transaction successful
def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded. 🥲")
        return False


# TODO 7: If the transaction is successful, then make coffee.
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\tHere is your {drink_name} ☕️. Enjoy!!😊")


# TODO 8: Write the report and notice to fill in resources if any of resources goes under the required amount
def write_report(ingredients):
    print(f"\tWater: {resources['water']}ml")
    print(f"\tMilk:  {resources['milk']}ml")
    print(f"\tCoffee: {resources['coffee']}g")
    print(f"\tMoney: ${profit}")
    for item in ingredients:
        if resources[item] < 100:
            print(f"Please fill in more {item}")


is_on = True
while is_on:
    option = input("Hello there 😃!! What would you like to drink today? (espresso/latte/cappuccino): ")
    if option not in ["latte", "espresso", "cappuccino", "off", "report"]:
        print("Please type in the correct name of the drink.")
    elif option == "off":
        is_on = False
    elif option == "report":
        write_report(resources)
    else:
        drink = MENU[option]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(option, drink["ingredients"])

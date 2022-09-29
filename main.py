from menu import MENU, resources

def coin_insert():
    p = float(input("How many pennies will you insert?: "))
    n = float(input("How many nickels will you insert?: "))
    d = float(input("How many dimes will you insert?: "))
    q = float(input("How many quarters will you insert?: "))
    total_cash = ((p*.01)+(n * .05)+(d * .1)+(q * .25))
    return total_cash

def coffee_machine():
    machine_on = True
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0
    while machine_on:
        user_choice = input("What would you like? Type 'espresso', 'latte', or 'cappuccino'.: ").lower()

        if user_choice == "off":
            print("The coffee machine has been turned off.")
            machine_on == False

        elif user_choice == "report":
            print(f"Water: {water}ml\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${money}")

        else:
            if water < MENU[user_choice]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
            elif milk < MENU[user_choice]["ingredients"]["milk"]:
                print("Sorry there is not enough milk.")
            elif coffee < MENU[user_choice]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
            else:
                user_amount = coin_insert()
                if user_amount < MENU[user_choice]["cost"]:
                    print("Sorry, not enough money. Money has been refunded.")
                elif user_amount > MENU[user_choice]["cost"]:
                    change = user_amount - MENU[user_choice]["cost"]
                    format_change = "{:.2f}".format(change)
                    print(f"Here is ${format_change} in change.")
                    water -= MENU[user_choice]["ingredients"]["water"]
                    milk -= MENU[user_choice]["ingredients"]["milk"]
                    coffee -= MENU[user_choice]["ingredients"]["coffee"]
                    money += MENU[user_choice]["cost"]
                    print(f"And your {user_choice} is ready. Enjoy!")
                else:
                    water -= MENU[user_choice]["ingredients"]["water"]
                    milk -= MENU[user_choice]["ingredients"]["milk"]
                    coffee -= MENU[user_choice]["ingredients"]["coffee"]
                    money += MENU[user_choice]["cost"]
                    print(f"Here is your {user_choice}. Enjoy!")



coffee_machine()
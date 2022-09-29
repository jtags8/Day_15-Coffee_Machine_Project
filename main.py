from menu import MENU, resources

def ingredient_check(choice, w, m, c):
    ###Checks if there are enough resources in the machine###
    if choice < w or choice < m or choice < c:
        return ("Not enough resources.")
def coin_insert():
    p = float(input("How many pennies will you insert?: "))
    n = float(input("How many nickels will you insert?: "))
    d = float(input("How many dimes will you insert?: "))
    q = float(input("How many quarters will you insert?: "))
    total_cash = ((p*.01)+(n * .05)+(d * .1)+(q * .25))
    return total_cash

# TODO #1: Prompt should show again after each completed action to serve next customer.
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
    # else:
    #     if water < MENU[user_choice][""]

# TODO #4: Check if resources are sufficient.
#   IF not enough, do not make drink, instead print "Sorry there is not enough ___."

# TODO #5: Process coins.
#   Need to calculate monetary value of coins inserted.
#   Prompt user to input coins used.
# TODO #6: Need to check if transaction is successful
#   Enough money entered? If not, should say "Sorry, not enough money. Money refunded."
#   Else, cost of drink gets added to machine as profit and reflect in report.
#   If too much money, need to give change. "Here is ___ in change." rounded to 2 decimals.
    user_amount = coin_insert()
    if user_amount < MENU[user_choice]["cost"]:
        print("Sorry, not enough money. Money has been refunded.")
    elif user_amount > MENU[user_choice]["cost"]
    else:




# TODO #7: Make coffee.
#   Deduct resources from machine resources.
#   Tell user "Here is your___. Enjoy!"


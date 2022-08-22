
MENU = {
    "espresso": {
        "ingredient": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 2.5,
    },
    "latte": {
        "ingredient": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "cappuccino": {
        "ingredient": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 1.5,
    },
}

resources= {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficent(order_ingredients):
    """Return True when order can be made, false if ingredientd are insufficent"""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True      

def process_coins():
    """return the total calculated from coins inserted"""
    print("print insert coins.")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.1
    total += int(input("how many nickels?: "))*0.05
    total += int(input("how many pennis?: "))*0.01
    return total

def is_transaction_successful(money_receive, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_receive >= drink_cost:
        change =round(money_receive-drink_cost,2)
        print(f"here is ${change} as change")
        global profit
        profit +=drink_cost
        return True
    else:
        print("sorry that is not enough money. Money Refunded")
        return False        

def make_coffee(drink_name, order_ingredients):
    """deduct the require ingredient from the resources"""
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
    print(f"here is your {drink_name} ☕")    


is_on = True
profit = 0

while is_on:
    choice = input("what would you like?(espresso/latte/capuccino) 'off/report' :")
    
    if choice =="off":
        is_on = False
    elif choice =="report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee :{resources['coffee']}ml")
        print(f"Money:{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficent(drink["ingredient"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredient"])

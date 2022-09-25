from tkinter import N, Menu


MENU = {
    "espresso": {
        "ingredients": {
            "milk":0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0.00,
}
paid=0.00
should_run=True


def check_resourse(drink):
    if MENU[drink]["ingredients"]["water"]<=resources["water"] and MENU[drink]["ingredients"]["milk"]<=resources["milk"] and MENU[drink]["ingredients"]["coffee"]<=resources["coffee"]:
        return True
    else:
        return False

def serve(drink):
    price=MENU[drink]["cost"]
    if paid<price:
        print("Sorry that's not enough money. Money refunded")
    else:
        change=paid-price
        resources["money"]+=paid
        resources["coffee"]-=MENU[drink]["ingredients"]["coffee"]
        resources["milk"]-=MENU[drink]["ingredients"]["milk"]
        resources["water"]-=MENU[drink]["ingredients"]["water"]
        print(f"Here is your change ${change}")
        print(f"Here is your {drink} ☕. Enjoy!")


def report():
    print("water:",resources["water"],"\nmilk:",resources["milk"],"\ncoffee:",resources["coffee"],"\nmoney:",resources["money"])
    return


while should_run:
    drink=input("What would you like? (espresso/latte/cappuccino: )")
    if drink=='report':
        report()
    elif drink=='off':
        should_run=False
    else:
        if check_resourse(drink):
            print("Please insert the coins.")
            q=int(input("how many quarters: "))
            d=int(input("how many dimes: "))
            n=int(input("how many nickles: "))
            p=int(input("how many pennies: "))
            paid=q*.25+d*.10+n*.05+p*.01
            paid=round(paid,2)
            print(f"You paid ${paid}")
            serve(drink)
        else:
            print(f"sorry insufficient resoures for {drink}. Try choosing other drink.")





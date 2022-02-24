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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
while True:
    odgovor_korisnika = input("What would you like? (espresso/latte/cappuccino): ").lower()
    money = 0
    if odgovor_korisnika == "report":
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f"profit: {profit}")

    if odgovor_korisnika == "off":
        print("Machine is shutting down!")
        break




    if odgovor_korisnika == "espresso":

        if resources["water"]< MENU["espresso"]["ingredients"]["water"] or resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Not enough resources :(")
            continue

        else:
            quarter_quantity = float(input("How much quarters do you input?: "))
            dime_quantity = float(input("How much dimes do you input?: "))
            nickel_quantity = float(input("How much nickles do you input?: "))
            penny_quantity = float(input("How much pennies do you input?: "))

            money = (quarter_quantity * 0.25) + (dime_quantity * 0.10) + (nickel_quantity * 0.05) + (penny_quantity * 0.01)

            if money < MENU["espresso"]["cost"]:
                print("Not enough money, your money will be refunded...")
                continue
            else:
                change = money - MENU["espresso"]["cost"]
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                profit += money
                profit -= change
                if change > 0:
                    print(f"Here is your change: {round(change,3)}")
                change = 0
                print(f"Here is your {odgovor_korisnika}, Enjoy!")



    if odgovor_korisnika == "latte":

        if resources["water"]< MENU["latte"]["ingredients"]["water"] or resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Not enough resources :(")
            continue

        else:
            quarter_quantity = float(input("How much quarters do you input?: "))
            dime_quantity = float(input("How much dimes do you input?: "))
            nickel_quantity = float(input("How much nickles do you input?: "))
            penny_quantity = float(input("How much pennies do you input?: "))

            money = (quarter_quantity * 0.25) + (dime_quantity * 0.10) + (nickel_quantity * 0.05) + (penny_quantity * 0.01)

            if money < MENU["latte"]["cost"]:
                print("Not enough money, your money will be refunded...")
                continue
            else:
                change = money - MENU["latte"]["cost"]
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                profit += money
                profit -= change
                if change > 0:
                    print(f"Here is your change: {round(change,2)}")

                print(f"Here is your {odgovor_korisnika}, Enjoy!")




    if odgovor_korisnika == "cappuccino":

        if resources["water"]< MENU["cappuccino"]["ingredients"]["water"] or resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Not enough resources :(")
            continue

        else:
            quarter_quantity = float(input("How much quarters do you input?: "))
            dime_quantity = float(input("How much dimes do you input?: "))
            nickel_quantity = float(input("How much nickles do you input?: "))
            penny_quantity = float(input("How much pennies do you input?: "))

            money = (quarter_quantity * 0.25) + (dime_quantity * 0.10) + (nickel_quantity * 0.05) + (penny_quantity * 0.01)

            if money < MENU["cappuccino"]["cost"]:
                print("Not enough money, your money will be refunded...")
                continue
            else:
                change = money - MENU["cappuccino"]["cost"]
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                profit += money
                profit -= change
                if change > 0:
                    print(f"Here is your change: {round(change,2)}")

                print(f"Here is your {odgovor_korisnika}, Enjoy!")






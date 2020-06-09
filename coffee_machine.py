water = 400
milk = 540
coffee = 120
cups = 9
money = 550

def output():
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")

while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "remaining":
        output()
    if action == "exit":
        break
    if action == "buy":
        buy_what = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if buy_what == "back":
            continue
        elif buy_what == "1":
            if water < 250:
                print("Sorry, not enough water!")
                continue
            elif coffee < 16:
                print("Sorry, not enough coffee beans!")
                continue
            elif cups < 1:
                print("Sorry, not enough disposable cups!")
                continue
            else:
                water -= 250
                coffee -= 16
                cups -= 1
                money += 4
        elif buy_what == "2":
            if water < 350:
                print("Sorry, not enough water!")
                continue
            elif milk < 75:
                print("Sorry, not enough milk!")
                continue
            elif coffee < 20:
                print("Sorry, not enough coffee beans!")
                continue
            elif cups < 1:
                print("Sorry, not enough disposable cups!")
                continue
            else:
                water -= 350
                milk -= 75
                coffee -= 20
                cups -= 1
                money += 7
        elif buy_what == "3":
            if water < 200:
                print("Sorry, not enough water!")
                continue
            elif milk < 100:
                print("Sorry, not enough milk!")
                continue
            elif coffee < 12:
                print("Sorry, not enough coffee beans!")
                continue
            elif cups < 1:
                print("Sorry, not enough disposable cups!")
                continue
            else:
                water -= 200
                milk -= 100
                coffee -= 12
                cups -= 1
                money += 6
        print("I have enough resources, making you a coffee!")
    if action == "fill":
        water += int(input("Write how many ml of water do you want to add: "))
        milk += int(input("Write how many ml of milk do you want to add: "))
        coffee += int(input("Write how many grams of coffee beans do you want to add: "))
        cups += int(input("Write how many disposable cups of coffee do you want to add: "))
    if action == "take":
        print(f"I gave you ${money}")
        money = 0
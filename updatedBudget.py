from datetime import datetime
import time


class Budget:
    #account = {"food_acc": 0, "cloth_acc": 0, "entertainment_acc": 0}
    food_acc = 0
    cloth_acc = 0
    entertainment_acc = 0

    def __init__(self):
        super().__init__()

    def func_budget(self):
        print("Start budgeting for your expenses")
        activitySelected = int(
            input(
                "Select:\n1. Deposit Funds\n2. Withdraw Funds\n3. Check Balance\n4. Transfer Funds\n"
            )
        )

        # userchoice
        if activitySelected == 1:
            Budget.deposit(self)
        elif activitySelected == 2:
            Budget.withdraw(self)
        elif activitySelected == 3:
            Budget.balance(self)
        elif activitySelected == 4:
            Budget.transfer(self)
        else:
            print("Invalid choice. Please try again")
            time.sleep(4)
            Budget.func_budget(self)

    #########  deposit funds to different categories ###########
    def deposit(self):
        print("Please deposit your funds to these categories")
        print("-" * 40)

        time.sleep(2)

        amount = float(input("How much would you like to spend on food? \n"))
        Budget.food_acc += amount
        amount = float(input("How much would you like to spend on Clothes? \n"))
        Budget.cloth_acc += amount
        amount = float(input("How much would you like to spend on entertainment? \n"))
        Budget.entertainment_acc += amount

    #########  withdraw funds from different categories ###########
    def withdraw(self):
        print("Withdraw your funds from these categories")
        choice = int(input("select:\n 1. Food\n2. Clothing\n3. Entertainments\n"))

        if choice == 1:
            amount = float(input("How much would you like to withdraw from food? \n"))
            if Budget.food_acc >= amount:
                Budget.food_acc -= amount
                print(f"Food Account balance:{Budget.food_acc}")
                Budget.func_budget(self)
            else:
                print("insufficient funds")

        elif choice == 2:
            amount = float(
                input("How much would you like to withdraw from Clothes? \n")
            )
            Budget.cloth_acc -= amount
            print(f"Clothing Account balance:{Budget.cloth_acc}")
            Budget.func_budget(self)
        elif choice == 3:
            amount = float(
                input("How much would you like to withdraw from entertainment? \n")
            )
            Budget.entertainment_acc -= amount
            print(f"Entertainment Account balance:{Budget.entertainment_acc}")
            Budget.func_budget(self)
        else:
            selectedOption = int(
                input("Invalid Choice. Select :\n 1. Withdraw\n 2. Menu\n")
            )
            if selectedOption == 1:
                Budget.withdraw(self)
            elif selectedOption == 2:
                Budget.func_budget(self)
            else:
                exit()

    #########  Check your balances in each categores ###########
    def balance(self):
        print(
            f"Your account Balance is: {Budget.cloth_acc+ Budget.food_acc + Budget.entertainment_acc}"
        )
        print(f"Food Balance: {Budget.food_acc}")
        print(f"Clothes Balance: {Budget.cloth_acc}")
        print(f"Entertainment Balancee: {Budget.entertainment_acc}")

        Budget.func_budget(self)

    #########  Tranfer funds to & from categores ###########
    def transfer(self):
        print("You can freely transfer funds from one category to another")
        tranferOption = int(
            input(
                "These are the available transfer otpions.\n Select: \n1. Food to Cloth\n2. Food to Entertainment\n3. Cloth to Entertainment\n4. Cloth to Food\n5. Entertainment to Food\n6. Entertainment to Cloth\n"
            )
        )
        if tranferOption == 1:
            print(f"Food Balance: {Budget.food_acc}")
            amount = float(input("How much would you like to transfer? \n"))
            if amount <= Budget.food_acc:
                Budget.food_acc -= amount
                Budget.cloth_acc += amount

            else:
                print("You do not have enough funds to Trasfer")
                Budget.func_budget(self)

        elif tranferOption == 2:
            print(f"Food Balance: {Budget.food_acc}")
            amount = float(input("How much would you like to transfer? \n"))
            if amount <= Budget.food_acc:
                Budget.food_acc -= amount
                Budget.entertainment_acc += amount
            else:
                print("You do not have enough funds to Trasfer")
                Budget.func_budget(self)

        elif tranferOption == 3:
            print(f"Cloth Balance: {Budget.cloth_acc}")
            amount = float(input("How much would you like to transfer? \n"))
            if amount <= Budget.cloth_acc:
                Budget.cloth_acc -= amount
                Budget.entertainment_acc += amount
            else:
                print("You do not have enough funds to Trasfer")
                Budget.func_budget(self)

        elif tranferOption == 4:
            print(f"Cloth Balance: {Budget.cloth_acc}")
            amount = float(input("How much would you like to transfer? \n"))
            if amount <= Budget.cloth_acc:
                Budget.cloth_acc -= amount
                Budget.food_acc += amount
            else:
                print("You do not have enough funds to Trasfer")
                Budget.func_budget(self)

        elif tranferOption == 5:
            print(f"Entertainment Balance: {Budget.entertainment_acc}")
            amount = float(input("How much would you like to transfer? \n"))
            if amount <= Budget.entertainment_acc:
                Budget.entertainment_acc -= amount
                Budget.food_acc += amount
            else:
                print("You do not have enough funds to Trasfer")
                Budget.func_budget(self)

        elif tranferOption == 6:
            print(f"Entertainment Balance: {Budget.entertainment_acc}")
            amount = float(input("How much would you like to transfer? \n"))
            if amount <= Budget.entertainment_acc:
                Budget.entertainment_acc -= amount
                Budget.cloth_acc += amount
            else:
                print("You do not have enough funds to Trasfer")
                Budget.func_budget(self)

        else:
            print("Invalid choice. Try again")
            Budget.transfer(self)


budgetA = Budget()
budgetA.func_budget()

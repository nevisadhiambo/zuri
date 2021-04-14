class Budget:  
    
    account_balance = 0
    def acc_balance(self):
        print(f'The net balance of your budget categories is {Budget.total_balance}')

    def __init__(self, category):
        self.category = category
        self.category_balance = 0

    def deposit(self):
        amount = float(input(f'How much do you want to deposit for {self.category} account\n'))
        self.category_balance += amount
        Budget.account_balance += amount
        print(f'Your account balance for {self.category} is {self.category_balance} ')

    def withdraw(self):
        amount = float(input(f'How much do you want to withdraw from  {self.category} account?\n'))
        self.category_balance -= amount
        Budget.account_balance -= amount

        print(f'You have {self.category_balance} left in your {self.category} account')
    
    def transfer(self, catB):
        amount = float(input(f'How much do you want to transfer to your {catB.category} account?\n'))
        self.category_balance -= amount
        catB.category_balance += amount

        print('Transfer successful!')
        print(f'You have left in {self.category_balance} in your {self.category} account and {catB.category_balance} in your {catB.category} account')
        

    def check_balance(self):
        print(f'You have {self.category_balance} remaining in your {self.category} account')

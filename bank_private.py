class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # приватная переменная

    def deposit(self, amount):
        if amount > 0:     # если amount больше 0
            self.__balance += amount   # прибавить к self.__balance amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:  # если amount больше 0 ,но меньше self.__balance
            self.__balance -= amount   # вычесть из self.__balance amount
        else: # или
            print('Недостаточно средств') # написать Недостаточно средств

    def get_balance(self):
        return self.__balance  # вернуть self.__balance

account = BankAccount(1000) # переменная account
account.deposit(500) # переменная account.deposit
print(account.get_balance()) # написать account.get_balance
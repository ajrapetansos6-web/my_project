class BankAccount:
    def __init__(self, balance, password):
        self.__balance = balance
        self.__password = password
        
    def deposit(self, amount, password):
        if password == self.__password and amount > 0:
            self.__balance += amount
            return self.__balance
        return "Wrong password or invalid amount"
        
    def withdraw(self, amount, password):
        if password == self.__password and 0 < amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        return "Wrong password or insufficient funds"
        
    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            return self.__password
        return "Wrong password"
        
    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        return "Wrong password"
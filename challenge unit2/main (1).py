class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"${amount} deposited successfully."
        else:
            return "Invalid amount for deposit."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"${amount} withdrawn successfully."
        elif amount > self.__account_balance:
            return "Insufficient funds."
        else:
            return "Invalid amount for withdrawal."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"

# Creating an instance of the BankAccount class
account1 = BankAccount("1234567890", "John Doe", 1000)

# Testing deposit and withdrawal functionality
print(account1.display_balance())  # Display initial balance
print(account1.deposit(500))        # Deposit $500
print(account1.withdraw(200))       # Withdraw $200
print(account1.withdraw(1500))      # Attempt to withdraw $1500 (insufficient funds)
print(account1.deposit(-100))       # Attempt to deposit a negative amount
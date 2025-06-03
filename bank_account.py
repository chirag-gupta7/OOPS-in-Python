class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance ):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be positive")
        
    def wishdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Withdrawal amount must be positive and less than or equal to the balance")
    def get_balance(self):
        return self.balance
    
chirag = BankAccount("Chirag", "Shah", "1234567890", "Savings", "1234", 1000.0)
chirag.deposit(96)
chirag.wishdraw(25)
print(f"Current balance: {chirag.get_balance()}")


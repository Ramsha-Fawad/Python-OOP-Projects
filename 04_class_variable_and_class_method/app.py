class Bank:
    bank_name = "Python Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")
        print(f"Bank Name: {Bank.bank_name}")

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


account1 = Bank("Ramsha", 5000)
account2 = Bank("Fawad", 3000)

print("---- Before changing bank name ----")
account1.display_account_info()
print()
account2.display_account_info()

Bank.change_bank_name("RFS National Bank")

print("\n---- After changing bank name ----")
account1.display_account_info()
print()
account2.display_account_info()

# def get_account_name(account):
#     return account["holder_name"]

class BankAccount:
    def __init__(self, holder_name, balance, account_type):
        self.holder_name = holder_name
        self.balance = balance
        self.type = account_type
        self.rates = {"Personal": 10, "Buisness": 50}
# attributes ^

    def pay_in(self, amount):
        self.balance += amount 
    
    #method: pay monthly fee(). it would take 50 from an account 
    def monthly_pay_out(self):
            self.balance -= self.rates[self.type]
        # if (self.type == "Buisness"):
        #     self.balance -= 50 
        # else:
        #     self.balance -= 10 
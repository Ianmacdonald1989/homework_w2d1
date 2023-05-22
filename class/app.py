from modules.bank_account import *

# l =[]
# #list^

# l.append(1)
# #method^ a function that belongs to a list 

# print(l)

# str = "hello, Jen!"

# print(str.lower())
# #lower^ puts everything lower case 

account = {
    "holder_name": "John",
    "balance": 500,
    "type": "Buisness"
}

# print(get_account_name(account))

johns_account = BankAccount("John", 500, "Buisness")
randolph_account = BankAccount("Randolph", 0, "Personal")
paul_account = BankAccount("Paul", 100000, "Personal")
print(johns_account.balance)
print(randolph_account.type)
print(paul_account.balance)
randolph_account.pay_in(100)
johns_account.monthly_pay_out()


print(randolph_account.balance)

paul_account.pay_in(1)

paul_account.monthly_pay_out()
print(paul_account.balance)

print(paul_account.balance)
print(johns_account.balance)




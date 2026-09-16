import random
import json

#vklad/výběr
#převody
#historie transakcí

def create_account():
    name_surname = input("Enter your full name: ")
    born = input("Enter your birthdate (dd-mm-yyyy): ")
    phone = input("Enter your phone number: ")

    try:
        with open("account-balance.json", "r") as f:
            accounts = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        accounts = []

    while True:
        acc = random.randint(10000, 99999)

        if not any(account["account-number"] == acc for account in accounts):
            break

    account = {
        "name_surname": name_surname,
        "born": born,
        "phone": phone,
        "account-number": acc,
        "state": "active",
        "balance": 0
    }

    accounts.append(account)

    with open("account-balance.json", "w") as f:
        json.dump(accounts, f, indent=4)

    print(f"Account created successfully!")


def insert_balance(acc_num, balance):
    with open("account-balance.json", "r") as f:
        accounts = json.load(f)

    for account in accounts:
        if account["account-number"] == acc_num:
            account["balance"] += balance

    with open("account-balance.json", "w") as f:
        json.dump(accounts, f, indent=4)

    print(f"Balance updated successfully!")

def withdraw(acc_num, balance):
    with open("account-balance.json", "r") as f:
        accounts = json.load(f)

    for account in accounts:
        if account["account-number"] == acc_num:
            account["balance"] -= balance

    with open("account-balance.json", "w") as f:
        json.dump(accounts, f, indent=4)

    print(f"Balance updated successfully!")



if __name__ == "__main__":
    create_account()
    #insert_balance(18365, 1000)
    #withdraw(18365, 500)

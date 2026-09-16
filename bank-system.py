import random
import json
#převody + historie transakcí

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


def insert_balance(acc_num, **kwargs):
    balance = kwargs.get("balance")
    if not balance:
        balance = input("Enter balance to be inserted: ")

    with open("account-balance.json", "r") as f:
        accounts = json.load(f)

    for account in accounts:
        if account["account-number"] == acc_num and account["state"] == "active":
            account["balance"] += int(balance)
        elif account["state"] == "inactive" or account["state"] == "deleted":
            print("Unable to insert balance due to account's state")

    with open("account-balance.json", "w") as f:
        json.dump(accounts, f, indent=4)

    print(f"Balance updated successfully!")


def withdraw(acc_num, **kwargs):
    balance = kwargs.get("balance")

    if not balance:
        balance = input("Enter balance to be withdrawn: ")

    with open("account-balance.json", "r") as f:
        accounts = json.load(f)

    for account in accounts:
        if account["account-number"] == acc_num and account["state"] == "active":
            account["balance"] -= int(balance)
        elif account["state"] == "inactive" or account["state"] == "deleted":
            print("Unable to withdraw balance due to account's state")

    with open("account-balance.json", "w") as f:
        json.dump(accounts, f, indent=4)

    print(f"Balance updated successfully!")



if __name__ == "__main__":
    #create_account()
    insert_balance(18365)
    withdraw(18365, balance = 500)

import random
import json
#tvorba účtu
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






if __name__ == "__main__":
    create_account()

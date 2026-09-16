import random
import json
import datetime


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


def write_record(sender, receiver, balance, type):
    try:
        with open("transfer-history.json", "r") as f:
            records = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        records = []


    record = {
        "from":sender["name_surname"],
        "to":receiver["name_surname"],
        "balance":balance,
        "date":datetime.datetime.now().isoformat(),
        "type":type
    }

    records.append(record)

    with open("transfer-history.json", "w") as f:
        json.dump(records, f, indent=4)


def insert_balance(acc_num, **kwargs):
    balance = kwargs.get("balance")
    is_transfer = kwargs.get("type")
    if not balance:
        balance = input("Enter balance to be inserted: ")

    with open("account-balance.json", "r") as f:
        accounts = json.load(f)

    for account in accounts:
        if account["account-number"] == acc_num and account["state"] == "active":
            account["balance"] += int(balance)
            if not is_transfer:
                write_record(account, account, balance, "insert balance")
        elif account["state"] == "inactive" or account["state"] == "deleted":
            print("Unable to insert balance due to account's state")

    with open("account-balance.json", "w") as f:
        json.dump(accounts, f, indent=4)

    print(f"Balance updated successfully!")


def withdraw(acc_num, **kwargs):
    balance = kwargs.get("balance")
    is_transfer = kwargs.get("type")

    if not balance:
        balance = input("Enter balance to be withdrawn: ")

    with open("account-balance.json", "r") as f:
        accounts = json.load(f)

    for account in accounts:
        if account["account-number"] == acc_num and account["state"] == "active":
            account["balance"] -= int(balance)
            if not is_transfer:
                write_record(account, account, balance, "balance withdraw")
        elif account["state"] == "inactive" or account["state"] == "deleted":
            print("Unable to withdraw balance due to account's state")

    with open("account-balance.json", "w") as f:
        json.dump(accounts, f, indent=4)

    print(f"Balance updated successfully!")


def transfer_balance(sender, receiver):
    balance = input("Enter balance to be transferred: ")
    with open("account-balance.json", "r") as f:
        accounts = json.load(f)
        for account in accounts:
            if account["account-number"] == sender and account["state"] == "active":
                sender = account
            elif account["account-number"] == receiver and not account["state"] == "deleted":
                receiver = account
            elif account["state"] == "deleted":
                print("Unable to transfer balance due to account's state")

    withdraw(sender["account-number"], balance = balance, type = True)
    insert_balance(receiver["account-number"], balance = balance, type = True)
    write_record(sender, receiver, balance, "balance transfer")


def list_user_transfers(user):
    try:
        with open("transfer-history.json", "r") as f:
            records = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        records = []

    with open("account-balance.json", "r") as accounts:
        db = json.load(accounts)
        for account in db:
            if account["account-number"] == user:
                name_surname = account["name_surname"]

    for record in records:
        if not record["from"] == name_surname and not record["to"] == name_surname:
            records.pop(records.index(record))

    print(records)



if __name__ == "__main__":
    #create_account()
    #insert_balance(18365)
    #withdraw(18365, balance = 500)
    transfer_balance(71815, 18365)
    list_user_transfers(18365)

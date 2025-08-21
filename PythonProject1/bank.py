import random
import json
from datetime import datetime
active_account = {}  # Will hold the currently active user’s info
def random_digit():
    return str(random.randint(0, 9))
def deposit(amount, active_account, data):
    active_account['balance'] += amount
    # Also update the matching record in the full data list
    for account in data:
        if account['card number'] == active_account['card number']:
            account['balance'] = active_account['balance']
            break
    with open("bank_details.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Deposited ${amount:.2f}. New balance: ${active_account['balance']:.2f}")
def withdraw(amount, active_account, data):
    if amount > active_account['balance']:
        print("Insufficient funds!")
        return
    active_account['balance'] -= amount
    # Update JSON record
    for account in data:
        if account['card number'] == active_account['card number']:
            account['balance'] = active_account['balance']
            break
    with open("bank_details.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Withdrew ${amount:.2f}. New balance: ${active_account['balance']:.2f}")
def banking():
    register_or_access_account = input(
        'Do you want to register a new account or do you want to access an account?\n'
    )

    if 'register' in register_or_access_account.lower():
        # Try to read existing file contents
        try:
            with open("bank_details.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        if not isinstance(data, list):
            data = [data]

        account_info = {}
        name = input('What name do you want this account to be under?\n')
        SSN = int(input('What Social Security Number do you want this account to be under?\n'))

        if len(str(SSN)) != 9:
            print(f'Social Security Numbers have to be 9 digits long; you entered a {len(str(SSN))}-digit SSN.')
        else:
            month_of_birth = int(input('What month were you born in (use the number form)?\n'))
            day_of_birth = int(input('What day were you born?\n'))
            year_of_birth = int(input('What year were you born?\n'))

            current_year = datetime.now().year
            age = current_year - year_of_birth

            if age < 18:
                print('You are not old enough to make a bank account')
            else:
                address = input("What is your address?\n")
                account_info['name'] = name
                account_info['SSN'] = SSN
                account_info['month of birth'] = month_of_birth
                account_info['day of birth'] = day_of_birth
                account_info['year_of_birth'] = year_of_birth
                account_info['age'] = age
                account_info['address'] = address

                CVC = ''.join(random_digit() for _ in range(3))
                account_info["cvc"] = CVC

                card_number = '69' + ''.join(random_digit() for _ in range(13))
                account_info['card number'] = card_number

                print(f'Remember these details\nCard Number = {card_number}\nCVC = {CVC}')
                account_balance = 0.00
                account_info['balance'] = account_balance

                # Append new account
                data.append(account_info)

                # Write back to JSON
                with open("bank_details.json", "w") as f:
                    json.dump(data, f, indent=4)
    elif 'access' in register_or_access_account.lower():
        try:
            with open("bank_details.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        if not isinstance(data, list):
            data = [data]

        name = input('What name is on the account?\n')
        card_number = input('What is the card number you were provided with?\n')
        CVC = input('What is the CVC you were provided with?\n')

        for account in data:
            if (str(account.get("name")) == name and
                str(account.get("card number")) == card_number and
                str(account.get("cvc")) == CVC):
                active_account = account.copy()  # store in dict for this session
                print(f"Welcome back, {active_account['name']}!")
                break
        else:
            print("Account not found or details incorrect.")
        repeat = 'y'
        while 'y' in repeat.lower():
            action = input('Do you want to\n1. Check account balance\n2. Deposit money into your account\n3. Withdraw money from your account?\n')
            if 'check' in action.lower() or '1' in action:
                print(f'You currently have ${active_account["balance"]} in your account.')
                repeat = input('Do you want to do anything else today?\n')
            elif 'deposit' in action.lower() or '2' in action:
                amount = float(input('How much money do you want to deposit into your account?\n$'))
                deposit(amount, active_account, data)
                repeat = input('Do you want to do anything else today?\n')
            elif 'withdraw' in action.lower() or '3' in action:
                amount = float(input('How much money do you want to withdraw from your account?\n$'))
                withdraw(amount, active_account, data)
                repeat = input('Do you want to do anything else today?\n')
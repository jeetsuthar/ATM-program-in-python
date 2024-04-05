import threading
import time


# ! need some information related to user Account
def info():
    Repeat = 0
    RepetitionTime = 1
    #! check User Name
    while Repeat < RepetitionTime:
        Name = input("Enter your  name :- ")
        if len(Name) == 0 or len(Name) < 3:
            print("⚠️ >>>>> Name must be required more then 3 character")
            RepetitionTime += 1
        else:
            Repeat = 0
            RepetitionTime = 1
            #! check Account Number
            while Repeat < RepetitionTime:
                Account_Number = input("Enter your Account Number :- ")
                if len(Account_Number) < 10 or len(Account_Number) > 10:
                    print("⚠️ >>>>> It's not a Valid Card or Account Number ")
                    RepetitionTime += 1
                else:
                    Repeat = 0
                    RepetitionTime = 1
                    #! check User account PIN number
                    while Repeat < RepetitionTime:
                        User_PIN = input("Enter 4-digit secret PIN number :- ")
                        if len(User_PIN) < 4 or len(User_PIN) > 4:
                            print("⚠️ >>>>> Invalid PIN Number")
                            RepetitionTime += 1
                        else:
                            Repeat = 0
                            RepetitionTime = 1
                            #! check Amount of money
                            while Repeat < RepetitionTime:
                                AmountMoney = input(
                                    "Enter Amount of money(Limitation 10,000) :- "
                                )
                                if len(AmountMoney) > 10000:
                                    print(
                                        "⚠️>>>>> Maximum Add limit exceeded. Please Add an amount within the allowed limit of 10,000 at a time."
                                    )
                                    RepetitionTime += 1
                                else:
                                    # ! store the all information into the yser_account.txt file
                                    fetch_data(
                                        Name, Account_Number, User_PIN, AmountMoney
                                    )
                                    break
                            Repeat += 1
                    Repeat += 1
            Repeat += 1
    Repeat += 1


# ! Add new Account
def fetch_data(name, account_number, account_pin, amount):
    account = {
        "Name": f'"{name}"',
        "Account-Number": str(account_number),
        "PIN": str(account_pin),
        "Amount": str(amount),  
    }
    data = "{"
    file = open("user_account.txt", "a+")

    for details in account.keys():
        data += f"'{str(details)}'" + ": " + str(account[details]) + ", "

    data = data[: len(data) - 2] + "}\n"
    file.write(data)
    time.sleep(1)
    print("Account Details Saved")
    time.sleep(0.5)
    print(
        "-----------------------------------------------------------------------------------"
    )
    file.close()


# ! withdraw Amount from user Account
def withdraw(savedName, SavedAmount, SavedPIN, a):
    withdrawalTurn = 0
    wrongTurns = 1
    while withdrawalTurn < wrongTurns:
        Withdraw_Amount = int(input("Enter Withdraw Amount: "))
        if Withdraw_Amount > int(SavedAmount):
            print("🙁 >>> Insufficient Balance")
            wrongTurns += 1
        elif Withdraw_Amount <= 0:
            print("⚠️ >>> Balance is less than or equal to Zero.")
            wrongTurns += 1
        else:
            TryPIN = 0
            wrongPIN = 1
            if TryPIN == 3:
                print("program executed")
                break
            while TryPIN <= wrongPIN:
                Account_PIN = int(input("Enter 4 digit PIN: "))
                if Account_PIN != int(SavedPIN):
                    print("⚠️ >>> Incorrect PIN")
                    if wrongPIN == 3:
                        TryPIN = 4
                        break
                    else:
                        wrongPIN += 1
                else:
                    time.sleep(1)
                    print("Processing.....")
                    time.sleep(2)
                    print("🙂 >>> Transaction completed Successfully. ")
                    updated_amount = int(SavedAmount) - Withdraw_Amount

                    # Update the amount in the data
                    updated_data = []
                    with open("user_account.txt", "r") as file:
                        data = file.readlines()
                        for line in data:
                            account_data = eval(line)
                            if account_data["Name"] == savedName:
                                account_data["Amount"] = str(updated_amount)
                            updated_data.append(str(account_data) + "\n")

                    # Write the updated data back to the file
                    with open("user_account.txt", "w") as file:
                        file.writelines(updated_data)

                    print("Your current balance is:", updated_amount)
                    print(
                        "\n----------------------------------- Restart the ATM ---------------------------------------\n"
                    )
                    start()

            TryPIN += 1
    withdrawalTurn += 1


# ! cash deposit into the existing Account
def cash_Deposit(SavedName, SavedAmount, SavedPIN):
    print(
        "------------------------------- CASH DEPOSIT ---------------------------------"
    )
    time.sleep(0.5)
    deposit_amount = int(input("Enter the amount of money to deposit: "))
    time.sleep(0.5)
    PIN = input("Enter your PIN: ")
    if int(PIN) == int(SavedPIN):
        if deposit_amount <= 0 or deposit_amount > 10000:
            time.sleep(0.5)
            print(
                "Invalid deposit amount: Please deposit at least 1 rupee and no more than 10,000 rupees at a time."
            )
        else:
            # Update the amount in the data
            updated_data = []
            with open("user_account.txt", "r") as file:
                data = file.readlines()
                for line in data:
                    account_data = eval(line)
                    if account_data["Name"] == SavedName:
                        account_data["Amount"] = str(
                            int(account_data["Amount"]) + deposit_amount
                        )
                    updated_data.append(str(account_data) + "\n")

            # Write the updated data back to the file
            with open("user_account.txt", "w") as file:
                file.writelines(updated_data)
            time.sleep(0.5)
            print(
                "Deposit successful. Your new balance is:",
                int(SavedAmount) + deposit_amount,
            )
            print(
                "\n----------------------------------- Restart the ATM ---------------------------------------\n"
            )
            start()
    else:
        time.sleep(0.5)
        print("Incorrect PIN")


# !Change the PIN
def change_PIN(SavedName, SavedAmount, SavedPIN):
    print(
        "------------------------------- CHANGE PIN -----------------------------------"
    )
    time.sleep(0.5)
    old_PIN = input("Enter your Old PIN number: ")
    if int(old_PIN) == int(SavedPIN):
        time.sleep(0.5)
        new_PIN = input("Enter new PIN Number: ")
        time.sleep(0.5)
        confirm_PIN = input("Enter new PIN Again: ")
        if new_PIN == confirm_PIN:
            # Read the contents of the file
            with open("user_account.txt", "r") as file:
                data = file.readlines()

            # Update the PIN in the data
            updated_data = []
            for line in data:
                account_data = eval(line)
                if account_data["Name"] == SavedName:
                    account_data["PIN"] = new_PIN
                updated_data.append(str(account_data) + "\n")

            # Write the updated data back to the file
            with open("user_account.txt", "w") as file:
                file.writelines(updated_data)
            time.sleep(0.5)
            print("Congratulations! Your new PIN has been updated successfully.")
            print(
                "\n----------------------------------- Restart the ATM ---------------------------------------\n"
            )
            start()
        else:
            time.sleep(0.5)
            print("Oops! Your PIN Numbers do not match. Please try again.")
    else:
        time.sleep(0.5)
        print("Incorrect Old PIN Number")


# !Continuo with existing Account
def get_value():
    print(
        "-----------------------------------------------------------------------------------"
    )
    time.sleep(0.5)
    value = int(input("Enter your existing Account Number :"))
    file = open("user_account.txt", "r")
    a = file.readlines()
    for elements in a:
        a = eval(elements)
        if value in a.values():

            # ! get data from the file
            SavedName = a["Name"]
            SavedAmount = a["Amount"]
            SavedPIN = a["PIN"]
            time.sleep(1)
            print(f"\n-------------------- WELCOME BACK, {SavedName.upper()} --------------------\n")
            # withdraw(SavedAmount, SavedPIN)
            time.sleep(0.5)
            print("Please select one of the following operations:")
            time.sleep(0.5)
            print(
                "1) Cash Withdrawal.\n2) Cash Deposit.\n3) PIN Change.\n4) Account Details."
            )
            time.sleep(0.5)
            selected = input("Select one digit out of the 1 to 4 : ")

            # ! option selection start to be here
            if selected == "1":
                time.sleep(0.5)
                withdraw(SavedName, SavedAmount, SavedPIN, a)
            elif selected == "2":
                time.sleep(0.5)
                cash_Deposit(SavedName, SavedAmount, SavedPIN)
                pass
            elif selected == "3":
                time.sleep(0.5)
                change_PIN(SavedName, SavedAmount, SavedPIN)
                pass
            elif selected == "4":
                time.sleep(0.5)

                PIN = input("Enter PIN Number : ")
                if int(PIN) == int(SavedPIN):
                    print(
                        "---------------------- ACCOUNT DETAILS ----------------------"
                    )
                    print(
                        "-------------------------------------------------------------"
                    )
                    time.sleep(0.5)
                    print(
                        f"|  Account Holder Name  | {SavedName}                     ||"
                    )
                    print(
                        "-------------------------------------------------------------"
                    )
                    time.sleep(0.5)
                    print(
                        f"|  Account Number       | {a['Account-Number']}                   ||"
                    )
                    print(
                        "-------------------------------------------------------------"
                    )
                    time.sleep(0.5)
                    print(
                        f"|  Current Bank Balance | {SavedAmount} Rs                      ||"
                    )
                    print(
                        "-------------------------------------------------------------"
                    )
                    time.sleep(2)
                    print(
                        "\n----------------------------------- Restart the ATM ---------------------------------------\n"
                    )
                    start()
                else:
                    print("Incorrect PIN ")
                    print(
                        "\n----------------------------------- Restart the ATM ---------------------------------------\n"
                    )
                    start()

    file.close()


# ! step1 : User choice
def start():
    print(
        "---------------------------------------------------------------------------------------"
    )
    print(
        "||                     🤖 WELCOME TO OUR ATM PROGRAM IN PYTHON 🤖                   ||"
    )
    print(
        "---------------------------------------------------------------------------------------"
    )
    time.sleep(0.5)
    print("\n1) Add new Account.")
    time.sleep(0.5)
    print("2) continue with existing Account (Default).")
    time.sleep(0.5)
    choice = input("Enter your Choice (1/2) : ")

    if choice == "1":
        info()
    else:
        get_value()


start()

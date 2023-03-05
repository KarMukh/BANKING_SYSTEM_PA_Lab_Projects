import Bank_Class


def user_page():
    print("Banking Record System")


menu_option = 0
num = 0
user_page()


while menu_option != 7:
    print("\n\tMenu")
    print("\t1. Open new account")
    print("\t2. Deposit amount")
    print("\t3. Withdraw amount")
    print("\t4. Transfer money")
    print("\t5. Display all accounts")
    print("\t6. Delete an account")
    print("\t7. Exit")
    print("\n\tPress 'Enter' and select your option from the Menu (1-8)")

    menu_option = input()
    if menu_option == '1':
        Bank_Class.creating_bank_account()
    elif menu_option == '2':
        num = int(input("\tEnter the account number: "))
        Bank_Class.deposit_amount(num)
    elif menu_option == '3':
        num = int(input("\tEnter the account number: "))
        Bank_Class.withdraw_amount(num)
    elif menu_option == '4':
        num1 = int(input("\tPlease input the account number you want money to withdraw from "))
        num2 = int(input("\tPlease input the account number you want money to transfer to "))
        transfer_amount = int(input("Please enter the amount you want to transfer "))
        Bank_Class.transfer_money()
    elif menu_option == '5':
        Bank_Class.display_all()
    elif menu_option == '6':
        num = int(input("\tEnter the account number: "))
        Bank_Class.delete_account(num)
        print(f"Bank account {num} has been deleted.")
    elif menu_option == '7':
        print("\tExiting Banking Record System")
        break
    menu_option = input("Press 'Enter' and select your option from the Menu (1-7)")
else:
    print("Invalid choice | Select your option from the Menu (1-7)")

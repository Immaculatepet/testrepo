balance = 2500  # set an initial balance value
pin = 4321  # Create a variable called pin

user_pin = int(input("kindly enter your PIN: ")) # Prompt the user to enter their pin

if user_pin == pin: # Confirm if the entered pin value matches
    # Display balance if the pin matches
    print(f"Your current balance is: ${balance}")

    # prompt the user if they would like to withdraw or deposit some money
    choice_made = input("Would you like to withdraw or deposit? (W/D): ")

    if choice_made.upper() == 'W':
        amount = float(input("Enter the amount you want to withdraw: ")) # Prompt the user to enter an amount to withdraw
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount   # Subtract the amount from balance and display updated balance
            print(f"Withdrawal successful. Your new balance is: ${balance}")
    elif choice_made.upper() == 'D':
        amount = float(input("Enter the amount you want to deposit: ")) # Prompt the user to enter an amount to deposit
        # Add the amount to balance and display updated balance
        balance += amount
        print(f"Deposit successful. Your new balance is: ${balance}")
    else:
        print("Incorrect choice.")
else:
    # Display a message if pins don't match
    print("Incorrect PIN. Enter a Valid PIN.")
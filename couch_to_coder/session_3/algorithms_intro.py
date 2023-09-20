# step by step to solve a problem or accomplish an end
pin = 1234 
balance = 5000 
 number_of_tries = 3

input_pin = input("kindly enter your PIN number!")

while(number_of_tries > 0):

    if(not input_pin.isdigit()):
        print("Invalid input, please enter a valid PIN number")
        break

    if (pin == int(input_pin)): 
        print("Your current balance is" + str(balance))
        break
    else:
        number_of_tries -= 1
        # guard clause
        if(number_of_tries == 0):
            break

    # RED - GREEN - REFACTOR
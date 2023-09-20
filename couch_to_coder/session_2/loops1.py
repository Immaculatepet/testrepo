pin_number =1234

input_pin = int( input("Enter your pin number:"))

while(input_pin != pin_number):
    print("Wrong number,try again!")
    input_pin = int( input())

print("Your balance is £500")

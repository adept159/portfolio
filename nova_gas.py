"""
NOVA gas program
"""
import random
def decide_fuel_price(fuel_choice):
    if fuel_choice.lower() == "r":
        return 3.351
    elif fuel_choice.lower() == "m":
        return 3.720
    elif fuel_choice.lower() == "p":
        return 4.042
    elif fuel_choice.lower() == "d":
        return 3.797

def revert_fuel_choice(fuel_choice):
    if fuel_choice.lower() == "r":
        return "Regular"
    elif fuel_choice.lower() == "m":
        return "Mid-Grade"
    elif fuel_choice.lower() == "p":
        return "Premium"
    elif fuel_choice.lower() == "d":
        return "Diesel"

def verify_credit_card(card_number):
    verify = False
    if len(card_number) == 15 or len(card_number) == 16:
        verify = True
    else:
        print("[-] Input did not meet length requirement.")

    for number in card_number:
        if number.isdigit() != True:
            print("[-] Input included a non-numerical value.")
            verify = False
            break

    if verify:
        return True
    else:
        return False

print("[+] Welcome to NOVA gas.")
start_quit = input("[!] Enter NOVAGas to start filling up or Goodbye to quit.")

while start_quit.lower() == "novagas":

    credit_card = input("[!] Please enter in a credit or debit card number.")

    while verify_credit_card(credit_card) != True:
        credit_card = input("[!] Please enter in a credit or debit card number.")

    print("[+] Credit card accepted.")

    car_wash_choice = input("[!] Would you like to purchase a car wash? You will get a 5 cent discount for every gallon purchased. Yes or No")
    if car_wash_choice.lower() == "yes":
        car_wash = True
        print("[+] Car wash is requested.")
    else:
        car_wash = False
        print("[+] Car wash is declined")

    print("[+] Please choose from the following fuel types:")
    print("[R] - Regular $3.351 per gallon.")
    print("[M] - Mid-Grade $3.720 per gallon.")
    print("[P] - Premium $4.042 per gallon.")
    print("[D] - Diesel $3.797 per gallon.")
    fuel_choice = input("[!] Please choose fuel type")

    while fuel_choice.lower() not in ("r", "m", "p", "d"):
        fuel_choice = input("[-] That is not a valid input, please choose again")

    fuel_price = decide_fuel_price(fuel_choice)

    gallon_amount = float(input("[!] How many gallons would you like to purchase?"))
    while gallon_amount <= 0:
        gallon_amount = input ("[-] The amount you selected must be greater than 0, please reselect.")

    if car_wash:
        discount = 0.05* gallon_amount
    else: discount = 0

    total_price = (fuel_price*gallon_amount) - discount

    print("-------------Receipt-------------")
    #print("Fuel chosen:" , revert_fuel_choice(fuel_choice))
    print("%-15s%15s" % ("Fuel chosen:", revert_fuel_choice(fuel_choice)))
    #print("Price per gallon $", fuel_price)
    print("%-15s%15f" % ("Price per gallon:", fuel_price))
    #print("Gallons purchased $", gallon_amount )
    print("%-15s%15f" % ("Gallons purchased:", gallon_amount))
    #print("Total before discount $", fuel_price*gallon_amount)
    print("%-15s%15f" % ("Total before discount $:", fuel_price*gallon_amount))
    #print("Car Wash Discount $", discount)
    print("%-15s%15f" % ("Car Wash Discount $:", discount))

    if car_wash:
        print("Car Wash Code :" , random.randint(100000, 999999))
    print("Total today is $", total_price)

    start_quit = input("[!] Would you like to fill up or quit? Enter NOVAGas or Goodbye.")

print("[+] See you next time partner.")

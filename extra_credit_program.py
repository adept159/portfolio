run_program = input("Enter Novagas or quit")

while run_program.lower() == "novagas":

    is_valid = False
    print("Please enter your telephone number.")
    phone = input("It must contain 10 digits")

    while not is_valid:
        if len(phone) == 10:
            correct_length = True
        else:
            correct_length = False

        for character in phone:
            if character.isdigit():
                check_number = True
            else:
                check_number = False
                break

        if correct_length == False and check_number == False:
            is_valid = False
        if not correct_length:
            print("Your telephone: ", phone, "does not have 10 characters")
        if not check_number:
            print("Your telephone: ", phone, "has characters other than a numeric value.")
            phone = input("Please enter your phone number again")
        if correct_length and check_number:
            is_valid = True

    print("continue processing from this point on")
    print("Are you a senior citizen?")
    senior = input()
    senior = senior.upper()
    print("Please choose from the following accomadations")
    print("(S) for Suite")
    print("(E) for Economy")
    cabin = input()
    cabin = cabin.upper()

    while cabin.upper() != 'S' or cabin.upper() != 'E':
        print("Invalid choice of cabin. Choose S or E:")
        cabin = input()

    if cabin == 'S':
        price = 2500.00
        cabin_description = "Suite"
    else:
        price = 1250.00
        cabin_description = "Cabin"
    print("Start having fun, but wait how many weeks (1 or more?")
    weeks = int(input())
    while weeks <1:
        print("Invalid entry. You must stay at least 1 week")
        weeks = int(input())
    total_bill_before_discount = price*weeks
    if senior.upper() == 'Y':
        senior_citizen_discount = total_bill_before_discount * .10
    else:
        senior_citizen_discount = 0
        total_bill_before_discount = total_bill_before_discount - senior_citizen_discount
    print("\n~~~~~~~~~~~~~~~~Please Pay~~~~~~~~~~~~~~~")
    print(f'{"Room Type" :20} {cabin_description:>20s}')






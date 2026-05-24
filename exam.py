number1 = ''
number2 = ''
choice = ''

while not isinstance(number1, int):
    try:
        number1 = int(input("Enter a first number:"))
    except:
        ValueError
        print("Invalid, please enter a NUMBER !")

while not isinstance(number2, int):
    try:
        number2 = int(input("Enter a second number:"))
    except:
        ValueError
        print("Invalid, please enter a NUMBER !")


while not isinstance(choice, int):
    try:
        choice = int(input(
            "To choose a type of calculation, type 1 for multiplication, 2 for division, 3 for substraction, and 4 for addition:"))
        if choice > 4:
            print("Invalid, enter 1, 2, 3 or 4")
            choice = 'invalid'
        elif choice < 1:
            print("Invalid, enter 1, 2, 3 or 4")
            choice = 'incorrect'
    except:
        ValueError
        print("Invalid, enter 1, 2, 3 or 4")

match choice:
    case 1:  # multiplication
        print(number1, "*", number2, "=", number1*number2)
        question = input(
            "Do you want the multiplication table of the two numbers you chosed ? (Answer by 'yes' or 'no')")
        if question == "yes":
            for a in range(21):
                print(number1, "*", a, "=", number1*a)
            print()
            for b in range(21):
                print(number2, "*", b, "=", number2*b)
        else:
            print("Ok enjoy your day.")

    case 2:  # division
        try:  # handle division by zero
            print(number1, "/", number2, "=", number1/number2)
        except:
            ZeroDivisionError
            print("Impossible to devide by zero")

        question2 = input(
            "Do you want the division table of the two numbers you chosed ? (Answer by 'yes' or 'no')")
        if question2 == "yes":
            for y in range(1, 21):
                print(number1, "/", y, "=", number1/y)
                print()
            for z in range(1, 21):
                print(number2, "/", z, "=", number2/z)
        else:
            print("Ok have a good day")

    case 3:  # substraction
        print(number1, "-", number2, "=", number1-number2)

    case 4:  # addition
        print(number1, "+", number2, "=", number1+number2)
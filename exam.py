num1=int(input("Enter a first number:"))
num2=int(input("Enter a second number:"))
choice=int(input("To choose a type of calculation, type 1 for multiplication, 2 for division, 3 for substraction, and 4 for addition:"))
match choice:
    case 1: #multiplication
        print(num1,"*",num2,"=",num1*num2)
        question=input("Do you want the multiplication table of the two numbers you chosed ? (Answer by 'yes' or 'no')")
        if question=="yes":
            for a in range (21):
                print(num1,"*",a,"=",num1*a)
            print()
            for b in range (21):
                print(num2,"*",b,"=",num2*b)
        else:
            print("Ok enjoy your day.3")

    case 2: #division
        print(num1,"/",num2,"=",num1/num2)
        question2=input("Do you want the division table of the two numbers you chosed ? (Answer by 'yes' or 'no')")
        if question2=="yes":
            for y in range (21):
                print(num1,"/",y,"=",num1/y) #handle division by zero
                print()
            for z in range (21):
                print(num2,"/",z,"=",num2/z)
        else:
            print("Ok have a good day")
            
        
    case 3: #substraction
        print(num1,"-",num2,"=",num1-num2)

    case 4: #addition
        print(num1,"+",num2,"=",num1+num2)
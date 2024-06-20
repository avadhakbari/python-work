from manager import *
from customer import *
import customer
while True:
    print("-----WELCOME TO FRUIT MARKET-----")
    print("1) Manager")
    print("2) Customer")

    roll = int(input("etner your roll :"))
    if roll == 1:
        print("1) add fruit stock") 
        print("2) view fruit stock")    
        print("3) update fruit stock")

   

        choice1 = int(input("enter your choice :"))
        if(choice1 == 1):
            add_fruit_stock()
            yn = str(input("you want to perform more option than press [yes] either press [no] :"))
            if yn == 'yes':
                continue
            else:
                print("!.........Thank You for Wisit........!")
                print("!.........Welcome Again..............!")
                break

        elif(choice1 == 2):
            view_fruit_stock()
            yn = str(input("you want to perform more option than press [yes] either press [no] :"))
            if yn == 'yes':
                continue
            else:
                print("!.........Thank You for Wisit........!")
                print("!.........Welcome Again..............!")
                break

        elif(choice1 == 3):
            update_fruit_stock()
            yn = str(input("you want to perform more option than press [yes] either press [no] :"))
            if yn == 'yes':
                continue
            else:
                print("!.........Thank You for Wisit........!")
                print("!.........Welcome Again..............!")
                break

        else:
            print("enter your valid choice number..")


    elif(roll == 2):
        print("1) view fruit stock")
        print("2) buy fruit")
        print("3) bill")
        choice2 = int(input("etner your choice :"))
        if(choice2 == 1):
            customer_view_stock()
            yn = str(input("you want to perform more option than press [yes] either press [no] :"))
            if yn == 'yes':
                continue
            else:
                print("!.........Thank You for Wisit........!")
                print("!.........Welcome Again..............!")
                break

        elif(choice2 == 2):
            customer_buy_stock()
            yn = str(input("you want to perform more option than press [yes] either press [no] :"))
            if yn == 'yes':
                continue
            else:
                print("!.........Thank You for Wisit........!")
                print("!.........Welcome Again..............!")
                break

        elif(choice2 == 3):
            customer_bill()
            yn = str(input("you want to perform more option than press [yes] either press [no] :"))
            if yn == 'yes':
                continue
            else:
                print("!.........Thank You for Wisit........!")
                print("!.........Welcome Again..............!")
                break

        else:
            print("enter valid choice")

    else:
        print("enter valid roll")

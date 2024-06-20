from manager import *
f = open("fruit.txt", "a")
dic3 = {}


def customer_view_stock():  #function declaration
    f_name = str(input("enter fruit name :"))
    if f_name in dic.keys():
        print("fruit name is", f_name)
        print("fruit quantity is :", dic[f_name]["quantity"])   #print quantity 
        print("fruit prise is", dic[f_name]["prise"])   #print prise


def customer_buy_stock():            #function declaration
    dic2 = {}  
    print("BUY STOCK")
    f_name = str(input("etner fruit name :"))
    if f_name in dic.keys():
        f_qty = int(input("enter fruit quantity :"))
        dic[f_name]["quantity"] -= f_qty   #substriction into stock
        f_prise = f_qty * dic[f_name]["prise"]
        dic2= {f_name :{"quantity": f_qty, "prise": f_prise}}    #multiple by stock amount
        global dic3
        dic3.update({f_name : {"quantity" : f_qty, "prise" : f_prise}})
        print(dic2)
        print("Availeble Fruit")
        print("-------------------------------")

    
def customer_bill():
    bill_number = int(input("Enter bill number: "))
    customer_name = input("Enter customer name: ")
    customer_no = input("Enter customer phone number: ")
    total_amount = 0

    with open("fruit.txt", "a") as f:
        print("".center(47, "-"), "BILL", "".center(47, "-"))
        f.write("-" * 47 + "BILL" + "-" * 47 + "\n")
        print("bill_number", bill_number)
        f.write(f"Bill Number: {bill_number}\n")
        print("customer name:", customer_name)
        f.write(f"Customer Name: {customer_name}\n")
        print("customer phone number :", customer_no)
        f.write(f"Customer Phone Number: {customer_no}\n")
        print("".center(100, "-"))
        f.write("-" * 100 + "\n")
        print("fruiit name \t \t \t quantity \t \t \t prise")
        f.write("Fruit Name \t\t Quantity \t\t Price\n")
        print("".center(100, "-"))
        f.write("-" * 100 + "\n")

        global dic3
        for i in dic3:
            qty = dic3[i]["quantity"]
            pr = dic3[i]["prise"]
            total_amount += pr
            print(f"{i} \t \t \t \t {qty} \t \t \t \t {pr}")
            f.write(f"{i} \t\t\t {qty} \t\t\t {pr}\n")

        print("".center(100, "-"))
        f.write("-" * 100 + "\n\n")
        print("total amount \t \t \t \t \t \t \t", total_amount)
        f.write(f"Total Amount: {total_amount}\n")
        print("".center(100,"-"))
        f.write("-" * 100 + "\n\n")
        f.close()

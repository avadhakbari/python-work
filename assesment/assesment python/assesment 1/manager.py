dic = {}
prise = 0

def add_fruit_stock():   #function declaration
        print("ADD FRUIT NAME")
        fruit_name = str(input("etner fruit name :"))
        fruit_qty = int(input("enter fruit quantity in (kg) :"))
        fruit_prise = int(input("enter fruit prise :"))
        print(f"fruit name : {fruit_name}\n fruit quantity : {fruit_qty}\n fruit prise : {fruit_prise}")   #print fruit stock 
        global dic     #gloabal variable
        dic.update({fruit_name :{"quantity" : fruit_qty, "prise": fruit_prise}})


def view_fruit_stock():   #function declaration
        print("VIEW FRUIT STOCK")
        print("-----AVAILABLE STOCK-----")
        for i in dic.keys():
            print("fruit name is :", {i})   #print fruit name
            print(i," fruit quantity is :", dic[i]["quantity"])   #print fruit quantity
            print(i," fruit prise is :", dic[i]["prise"])      #print fruit prise
            print("---------------------------------")


def update_fruit_stock():     #function declaration 
        print("UPDATE FRUIT STOCK")
        n_fruit = str(input("enter fruit name :"))       #input fruit name
        if n_fruit in dic.keys():          #add fruit in stock using if condition
            q_fruit = int(input("entr fruit quantity :"))
            dic[n_fruit]["quantity"] += q_fruit      #add quantity in stock 
 


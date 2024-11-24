# Authentication password
passwords={'admin':'admin1234','staff':''}
def enter_pwd():
    username=input("Enter your Username")
    pwd=input("Enter your Password")
    while pwd != passwords[username]:
        pwd=input("wrong password, Enter again")
    print("Access Granted Welcome!!")

# Update password
def update_pwd():
    import random
    otp=random.randint(10000,99999)
    print(otp)
    e_otp=int(input("enter otp"))
    if otp==e_otp:
        username=input("Enter Username")
        pwd=input("New Password")
        cpwd=input("Confirm Password")
        while pwd!=cpwd:
            cpwd=input("Password mismatching enter corrently")
        passwords[username]=cpwd
        print("Password Changed Successfully")
    elif otp!=e_otp:
        print("Wrong otp, resend otp and try again")

#Initiating individual functions

# function to display stock
def display_stock():
    for shoe,values in shoe_stock.items():
        print(f" {shoe} - price: ₹{values['price']}, quantity: {values['quantity']}")
        print()
    main_menu()

#function to add a new shoe
def new_shoe():
    shoe_name=input("enter the shoe name")
    shoe_price=float(input("enter the shoe price"))
    shoe_quantity=int(input("enter the quantity"))
    if shoe_name in shoe_stock:
        print(f'\'{shoe_name}\' is already in warehouse, use update_shoe to change the quantity')
    else:
        shoe_stock[shoe_name] = { "price":shoe_price, "quantity":shoe_quantity}
        print(f"{shoe_name} has been added to the stock")
        print()
    main_menu()

# function to update shoes
def update_shoe():
    shoe_name=input("enter the shoe name")
    if shoe_name in shoe_stock:
        change=input("Do You want to change the quantity")
        if change == "yes":
            q=int(input("enter updated quantity"))
            shoe_stock[shoe_name]['quantity'] +=q
            print(f'{q} quantity of {shoe_name} has been added')
            change=input("Do You want to change the price")
        elif change == "yes":
            p=float(intput("enter updated price"))
            shoe_stock[shoe_name]['price']=p
            print(f'price of {p} for {shoe_name} has been changed')
    else:
        print(f'{shoe_name} is not in stocks choose add new shoe feature')
    print()
    main_menu()

# function to sell shoes
def sell_shoe():
    shoe_name=input("enter the shoe name")
    q=int(input("enter the quantity"))
    worth=shoe_stock[shoe_name]['price']*q
    if q <= shoe_stock[shoe_name]['quantity']:
        shoe_stock[shoe_name]['quantity']-=q
        print(f'{q} {shoe_name} shoes worth of ₹{worth} sold')
        sell=input("Do You want sell other shoes")
    elif sell == "yes":
       sell_shoe()
    else:
        pass
    print()
    main_menu()

# main menu or home page
def main_menu():
    print("1.Display Stock\n2.Add newShoe\n3.Update Shoe\n4.Sell Shoe\n5.Exit")
    choice=int(input("Enter the choice 1-5"))
    print()
    if choice == 1:
        display_stock()
    elif choice == 2:
        new_shoe()
    elif choice == 3:
        update_shoe()
    elif choice == 4:
        sell_shoe()
    elif choice == 5:
        print("Exited from main menu")
    else:
        print("please enter the choice accodingly")     
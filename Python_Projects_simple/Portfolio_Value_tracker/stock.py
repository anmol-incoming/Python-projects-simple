def stock_update_add(all_users,current_user):
    stock_name=input("Enter the name of the stock you own :-")
    price=float(input("Enter the current price of the stock in ₹:-"))
    quantity=float(input("Enter the quantity of that stock you own:-"))
    all_users[current_user]["Portfolio"][stock_name]={
        "Price":price,
        "Quantity Owned":quantity

        }
    print(f"{current_user}.The Stock has been added/Updated to your account.")


    
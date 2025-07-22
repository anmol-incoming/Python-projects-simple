from save_load import load_user_data,save_load
def user_login():
    all_users=load_user_data()
    check=input("""Do you have a acccount:
                    1.Yes
                    2.No:-""")
    if check.isdigit():
        if check=="1":
            current_user=input("Enter your username:-")
            password=input("Enter your password:-")
            if current_user in all_users and password==all_users[current_user]['Pin']:
                print(f'Welecome Back {current_user}.')
                return all_users,current_user
            else:
                print("Incorrect Password or Username.")
                return user_login()

        if check=="2":
            while True:
                current_user=input("Enter your username:-")
                print("Checking username is availabe or not......")
                if current_user in all_users:
                    print("User name already exist. Try another username.")
                    continue
                else:
                    while True:
                        password=input("Enter atleast a 4 digit password:-")
                        if password.isdigit():
                            all_users[current_user]={
                                'Pin':password,
                                'Portfolio':{}

                            }
                            while True:
                                stock_check=input("""Do you own any stocks currently.You can also add later or update it. :-
                                                        1.Yes
                                                        2.No:-""")
                                if stock_check.isdigit():
                                    if stock_check=="1":
                                        stock_name=input("Enter the name of the stock you own :-")
                                        price=float(input("Enter the current price of the stock ₹:-"))
                                        quantity=float(input("Enter the quantity of that stock you own:-"))
                                        all_users[current_user]["Portfolio"][stock_name]={
                                            "Price":price,
                                            "Quantity Owned":quantity

                                        }
                                        print(f"{current_user}.The Stock has been added to your account.")
                                        save_load(all_users)
                                    

                                    elif stock_check=="2":
                                        print(f'{current_user}. Your account has been created.')
                                        save_load(all_users)

                                else:
                                    print("Invalid Entry.")
                                    continue
                                break
                        else:
                            print("Invalid Entry")
                            continue
                        break
    
                break

    return all_users,current_user

                    
                

                

    
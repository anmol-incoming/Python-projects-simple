from save_load import load_user_data,save_load
def user_account_creation():
    user_dict=load_user_data()
    account=input("""Do you have an account:-
                  1.Yes
                  2.No""")
    
    if account =="1":
        name=input("Enter your name :-")
        password=int(input('enter the 4 digit password:-'))
        if name in user_dict and str(password) ==user_dict[name]['Password']:
            print(f"Welecome Back {name} !!!")
            return user_dict,name
        else:
            print("Incorrect Username or Password.Please try again")
            return  user_account_creation()
    
    elif account=="2":
        new_user_name=input("Enter Your name:-")
        while True:
            new_user_password=input("Create Your 4 digit password:-")
            if new_user_password.isdigit():
                print("Checking password...")
                if len(new_user_password)>4:
                    print("Password length is too Big.Expceted 4 digit.")
                    continue
                elif len(new_user_password)<4:
                    print("Password length is too short")
                    continue
                elif len(new_user_password)==4:
                    print("Account created Successfully")
                    
                     
                    while True:
                        min_amount=input("Enter the minimum Balance amount of atleast ₹ 6000:- ")
                        if min_amount.isdigit() :
                            min_amount=int(min_amount)
                            if min_amount>=6000:
                                print(f'Balance of ₹ {min_amount} added to your account succesfully')
                                user_dict[new_user_name]={

                                    "Password":new_user_password,
                                    "Amount":min_amount,
                                    "Transction History":[]}
                                
                                save_load(user_dict)
                                break
                   
                            else:
                                print("Insufficient amount!!!")
                                continue
                        else:
                            print("Invalid Amount Entered.")
                            continue
            else:
                print("Error!!!.Make sure password is a 4 digit number.")
                continue
            break
    return user_dict, new_user_name


from datetime import datetime
def user_deposit (user_dict,current_user) :
    amount_deposit=input("enter the amount you want to deposit in ₹:- ")
    if amount_deposit.isdigit():
        amount_deposit=int(amount_deposit)
        user_dict[current_user]["Amount"] += amount_deposit
        print(f'Amount of ₹{amount_deposit} deposited successfully to your account.')
        user_dict[current_user]["Transction History"].append({
            'type':"Deposit",
            'amount':amount_deposit,
            'time':datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        })
        
    else:
        print("Invalid amount entered.")
   
    

    





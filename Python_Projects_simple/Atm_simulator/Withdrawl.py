
from datetime import datetime
def withdrawl(user_dict,current_user):
    amount_withdrawl=input ("enter the amount you want to withdrawl in ₹:- ")
    if amount_withdrawl.isdigit():
        amount_withdrawl=int(amount_withdrawl)
        if amount_withdrawl > user_dict[current_user]["Amount"]:
            print("Insufficient balance")
        else:
            user_dict[current_user]["Amount"] -= amount_withdrawl
            print(f'Amount of ₹{amount_withdrawl} withdrawn successfully from your account.')
        user_dict[current_user]["Transction History"].append({
            'type':"Withdrawl",
            'amount':amount_withdrawl,
            'time':datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        })

        
    else:
        print("Invalid amount entered.")
    
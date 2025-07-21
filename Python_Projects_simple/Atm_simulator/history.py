def user_history(user_dict,current_user):
    if user_dict[current_user]["Transction History"]==[]:
        print("There are no transction yet.")
    else:
        print(f"{current_user} your Transction History is Diplayed Below:-")
        for i,transction in enumerate(user_dict[current_user]["Transction History"],1):
            print(f"{i}.{transction['type']} of ₹{transction['amount']} on {transction['time']} ")
 

    


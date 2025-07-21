from deposit import user_deposit
from user_info import user_information
from Withdrawl import withdrawl
from history import user_history
from save_load import save_load
def user_menu(user_dict,current_user):
    while True:
        user_display=input("""Enter the service you want to perform
                                1.Deposit
                                2.Withdrawl
                                3.User Transction History
                                4.Check Your info/Balance
                                5.Exit""")
        if user_display=="1":
             user_deposit(user_dict,current_user)
        elif user_display=="2":
             withdrawl(user_dict,current_user)
        elif user_display=="3":
             user_history(user_dict,current_user)
        elif user_display=="4":
             user_information(user_dict,current_user) 
        elif user_display=="5":
            return "Thank you for using our service. Hope you have a great day."
        save_load(user_dict)
     
    

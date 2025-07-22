from stock import stock_update_add
from user_portfolio import show_portfolio
from total_portfolio_value import total_value
from save_load import save_load
def menu(all_users,current_user):
    while True:
        user_selection=input("""Choose which service you want:-
                                1.Add/Upadte Stock
                                2.Check your Portfolio
                                3.Calculate your total portfolio value
                                4.logout """)
        if user_selection.isdigit():
            if user_selection=="1":
                stock_update_add(all_users,current_user)
            elif user_selection=="2":
                show_portfolio(all_users,current_user)
            elif user_selection=="3":
                total_value(all_users,current_user)
            elif user_selection=="4":
                return f"Logged out scuccessfully.Thank you.Hope you have a great day {current_user}."
        else:
            print("Invalid value entered.Expected 1 to 4.")
        
        save_load(all_users)




    
from user_input import user_account_creation
from menu import user_menu

def main():
    user_dict,current_user=user_account_creation()
    result=user_menu(user_dict,current_user)
    print(result)

main()
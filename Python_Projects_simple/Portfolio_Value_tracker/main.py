from user_menu import menu
from user_login import user_login

def main():
    all_users,current_user=user_login()
    result=menu(all_users,current_user)
    print(result)
    
main()
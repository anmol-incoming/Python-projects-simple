def show_portfolio(all_users,current_user):
    print(f"{current_user}.Your portfolio:-")
    if all_users[current_user]['Portfolio']=={}:
        print("You dont have any stock added to your Portfolio. Please add some stock .")
    else:
        for i,(key,value) in enumerate(all_users[current_user]['Portfolio'].items(),1):
            print(f'{i}.{key}')
            print(f"Price: ₹{value['Price']}")
            print(f"Quantity Owned: {value['Quantity Owned']}")


def total_value(all_users,current_user):
    if all_users[current_user]['Portfolio']=={}:
        print(f"{current_user}.No stock to calculate.Please add some stocks.")
    else:
        print(f"{current_user}.Your calculated Portfolio Value:-")
        total_value=0
        for i,(key,value) in enumerate(all_users[current_user]['Portfolio'].items(),1):
            print(f'{i}.{key}')
            price=value["Price"]
            qty=value['Quantity Owned']
            total=price*qty
            print(f"Total value of the stock:- ₹{total}")
            total_value += total
        print(f'Your total/Overall Portfolio value is:- ₹{total_value}')







    


def user_information(user_dict,current_user):
    print("Your Information and Balance is:-")
    print(f"Your name :{current_user}")
    for key,value in user_dict[current_user].items(): 
        if key=="Transction History":
            continue     
        elif key=="Amount":
            print(f'{key}: ₹{value}')   
        else:
            print(f'{key}:{value}')
            

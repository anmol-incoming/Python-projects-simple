def dice_input():
    while True:
        dice_roll=input("Enter how many times do you want to run dice roll simulation:-")
        if dice_roll.isdigit():
            dice_roll_num=int(dice_roll)
            break 
        else:
            print("Invalid input Enter number more than 0")

    return dice_roll_num









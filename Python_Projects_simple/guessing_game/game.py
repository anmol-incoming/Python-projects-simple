import random 
def guessing_game(your_guess,random_number):
    count=1
    while your_guess != random_number:
        if your_guess>100:
            print("Please Guess the number between 1 to 100 only")
            count+=1      
        elif your_guess<random_number:
            print("Guess a higher number")
            count+=1
        elif your_guess>random_number:
            print("Guess a lower number ")
            count+=1
        your_guess=int(input("Please Guess again:"))
    if your_guess==random_number:
        return f'Congratulation you have guessed the number correctly.It took you {count} attempts.'
random_number=random.randint(1,100)
your_guess=int(input("Enter any number between 1 to 100:"))
result=guessing_game(your_guess,random_number)
print(result)

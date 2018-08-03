import random


while True:
    user_pick = input('Pick rock(1), paper(2), or scissors(3) or type "end" to end the game:  ')
    
    options = ["rock!", "paper!", "scissors!"]
    if int(user_pick) > len(options) and int(user_pick) > 0:
        print("you didn't pick a number?!")
    else:
        print("you picked", options[int(user_pick)])
    
    computer_pick = ['rock', 'paper', 'scissors']
    print('Computer picks ' + random.choice(computer_pick) + "!")
    
    


    
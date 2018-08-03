import random


while True:
    user_pick = input('Pick rock(0), paper(1), or scissors(2): ')
    
    options = ["rock!", "paper!", "scissors!"]
    if int(user_pick) > len(options) and int(user_pick) > 0:
        print("you didn't pick a number?!")
    else:
        print("you picked", options[int(user_pick)])
    
    computer_pick = ['rock', 'paper', 'scissors']
    print('Computer picks ' + random.choice(computer_pick) + "!")
    
    break

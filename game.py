import random


while True:
    user_pick = input('Pick rock(1), paper(2), or scissors(3) or type "end" to end the game:  ')
    
    if user_pick == '1':
        print('you picked rock!')
    elif user_pick == '2':
        print('you picked paper!')
    elif user_pick == '3':
        print('you picked scissors!')
    else:
        print("you didn't pick a number?!!")
    
    computer_pick = ['rock', 'paper', 'scissors']
    print('Computer picks ' + random.choice(computer_pick) + "!")
    
    if user_pick == "end":
        break
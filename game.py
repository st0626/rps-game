import random

name = "Scotty"

while name == "Scotty":
    user_pick = input('Pick rock(1), paper(2), or scissors(3):  ')
    computer = random.randint(1,3)
    if user_pick == '1':
        print('you picked rock!')
    elif user_pick == '2':
        print('you picked paper!')
    elif user_pick == '3':
        print('you picked scissors!')
    else:
        print("you didn't pick a number?!!")
    
    
    if computer == 1:
        print('computer picks rock!')
    elif computer == 2:
        print('computer picks paper!')
    elif computer == 3:
        print('computer picks scissors!')
    else:
        print("computer didn't pick a number!")
    break


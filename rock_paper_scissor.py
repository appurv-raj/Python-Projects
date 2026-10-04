import random
computer_wins = 0
user_wins = 0

options = ['rock', 'paper', 'scissors']
while True:
    user_input = input('Type rock,paper,scissors or type q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue   # this is to repeat the loop if you type other than R,P,S

    random_number = random.randint(0,2)
    computer_pick = options[random_number]

    if computer_pick == 'rock' and user_input == 'rock' :
        print("it's a DRAW")
    elif computer_pick == 'rock' and user_input == 'paper' :
        print('Computer WON')
        computer_wins += 1
    elif computer_pick == 'rock' and user_input == 'scissors' :
        print('Computer WON')
        computer_wins += 1

    elif computer_pick == 'paper' and user_input == 'rock':
        print('Computer WON')
        computer_wins += 1
    elif computer_pick == 'paper' and user_input == 'paper':
        print("it's a DRAW")
    elif computer_pick == 'paper' and user_input == 'scissors':
        print('User WON')
        user_wins += 1

    elif computer_pick == 'scissors' and user_input == 'rock':
        print('User WON')
        user_wins += 1
    elif computer_pick == 'scissors' and user_input == 'paper':
        print('Computer WON')
        computer_wins += 1
    elif computer_pick == 'scissors' and user_input == 'scissors':
        print("it's a DRAW")

print (f'Computer Won : {computer_wins}')
print(f'User Won: {user_wins}')
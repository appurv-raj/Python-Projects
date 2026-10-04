import random 

top_range = input('Enter a number: ')

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print('Please type a number that should be greater than 0.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0,top_range)
guessess = 0

while True:
    guessess += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print(f'CORRECT! You got it in {guessess} guessess')
        break
    elif user_guess > random_number:
        print('WRONG! You are higher, go Low')
    else:
        print('WRONG! You are lower, go High')


print('This is a Quiz Game!')

playing = input('do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("let's Start!!")
score = 0

answer = input('Who is the PM of India? ')
if answer.lower() == 'narendra modi':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input('What is the full form of CPU? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input('What does RAM stands for? ')
if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input('What does PSU stands for? ')
if answer.lower() == 'power supply unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

print(f'You got {score} out of 4')
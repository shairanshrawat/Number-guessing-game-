import random
play_game='y'

while play_game== 'y':
    answer = random.randint(1,100)
    try_number = int(input('Guess a number between 1 and 100:'))
    counter =1

    while try_number != answer:
        if try_number > answer:
            print('Your number is too larger. Try again!!!')
        if try_number < answer:
            print('Your number is soo small. Try again!!')
        try_number = int(input('Guess a number between 1 and 100:'))
        counter+= 1
    print('YAY..You got it!!! You tried ' + str(counter) + ' times')
    play_game=input('Wanna continue?')

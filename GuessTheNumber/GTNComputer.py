import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))

        if guess < random_number:
            print('OOps Guess again! Too low')
        
        elif guess > random_number: 
            print('OOPS Guess again! Too high')
        
    
    print(f'Congratulations! You guessed {random_number} correctly!')

def chooseDifficulty(): 
    highest_number = int(input('What is the highest number I can choose? example for 1-10 pick 10: '))

    guess(highest_number)

chooseDifficulty()
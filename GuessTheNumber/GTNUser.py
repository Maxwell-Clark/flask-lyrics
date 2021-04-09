import random

def computerGuess(x):
    low = 1
    high = x
    feedback = ' '
    while feedback != 'c': 
        if low != high: 
            guess = random.randint(low, high)
        else:
         guess = low
        
        feedback = input(f'is {guess} Too Low? (L), Too High? (H), or is it correct? (C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    
    print(f'You Stupid Human! The Computer can Guess any number! I AM VICTORIOUS!')


def chooseDifficulty():
    difficulty = int(input(f'I can Guess any number. what is the max limit? Ex 1-100 input 100: '))
    input(f'I will now pick a number between 1 - {difficulty}, Prepare to be amazed filthy Human.')
    input('press space to begin')
    computerGuess(difficulty)

chooseDifficulty()

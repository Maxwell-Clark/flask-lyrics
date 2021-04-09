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

computerGuess(50)
        
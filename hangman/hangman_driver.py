import re
import pandas as pd
from player import Player

# return indices of char occuring in string
def find(string, ch):
    return [i for i, ltr in enumerate(string) if ltr == ch]

if __name__ == '__main__':
    # initialize player with given dict
    player = Player(pd.read_csv(input('Absolute path to dict file: '), header=None, names=['word']))
    
    # max tries
    turns = input('Enter max tries (default=6), for default leave blank: ')
    turns = int(turns) if turns else 6
    
    word2guess = input('Enter any word available in the dictionary: ')
    
    # filter words by the given length
    player.filt_len(len(word2guess))
    
    # initial state
    state = ['_']*len(word2guess)
    print(f'{state} missed:\n')
    
    missed = []
    while turns > 0:
        # get next guess
        guess = player.make_guess()
        print(f'guess: {guess}\n')
        
        # refresh state
        if guess in word2guess:
            if guess not in state:
                for ind in find(word2guess, guess): state[ind] = guess
            else: print('You already guessed that\n'); turns -= 1
        
        # refresh missed list
        else:  
            print('You already guessed that\n') if guess in missed else missed.append(guess)
            turns -= 1
        
        # print current state
        print(' '.join(state) , 'missed:', ','.join(missed), end='\n')
        
        # Outcome
        if ''.join(state) == word2guess: print('\nYou have won');break
        
        # filter words by guess
        player.filt_guess(guess, state)
        
    # Outcome
    if turns == 0: print('\nSorry you lost')
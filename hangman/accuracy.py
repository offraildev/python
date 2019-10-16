import re
import time
from multiprocessing import Pool
import numpy as np
from itertools import repeat
import pandas as pd
from player import Player

# return indices of char occuring in string
def find(string, ch):
    return [i for i, ltr in enumerate(string) if ltr == ch]

def run_game(word2guess, words_df):
    # initialize player with given dict
    player = Player(words_df)
    
    # max tries
    turns = 6
    
    # initial state 
    state = ['_']*len(word2guess)
    
    # filter words by the given length
    player.filt_len(len(word2guess))
  
    while turns > 0:
        # get next guess
        guess = player.make_guess()
        
        # refresh state
        if guess in word2guess:
            if guess not in state:
                for ind in find(word2guess, guess): state[ind] = guess
            else: turns -= 1
        else: turns -= 1
        
        if ''.join(state) == word2guess: 
            #print('\nCorrect')
            flag = True
            break
        
        # filter words by guess
        player.filt_guess(guess, state)
        
    # Outcome
    if turns == 0: 
        #print('\nWrong')
        flag = False
    
    return flag

if __name__ == '__main__':
    pool = Pool(10)
    words_df = pd.read_csv(input('Absolute path to dict file: '), header=None, names=['word'])
    start_time = time.time()
    correct = pool.starmap(run_game, zip(words_df.word.values, repeat(words_df)))
    accuracy = np.mean(correct)
    print(f'Solver Accuracy: {accuracy}')
    print('Time taken {} minutes '.format(round((time.time() - start_time)/60, ndigits=2)))
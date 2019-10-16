Task 1:
-------

For the Hangman Solver I used a greedy letter-frequency algorithm which is as follows:

	Assumptions: The word is drawn from a particular dictionary

	Algorithm:
		- We know the number of letters in the word to be guessed
		- Filter all words in the dictionary that do not have the correct number of letters.
		- Guess the not-yet-guessed letter which occurs in the largest number of words in the remaining 
		  subset of the dictionary.(take the first if there is a tie)
		- If the letter occurs, we know its location.
		- If the letter does not occur, we know it does not occur in the word.
		- Filter all words in the dictionary subset that do not fit exactly this correct pattern, and repeat.


Running Instructions:
---------------------
- place the hangman_driver.py and player.py in same path
- run the hangman_driver.py and follow the given instructions


Task 2:
-------

Instead of printing if word guessed correctly or not, a list of bool values (true correct) is returned for convenience. 

Running Instructions:
---------------------
- place the accuracy.py and player.py in same path
- run the accuracy.py and follow the given instructions
class Player:
	def __init__(self, words_df):
		self.words_df = words_df
		self.keys = set('abcdefghijklmnopqrstuvwxyz')
		self.guessed = ''

	# filter dict by given length of word2guess
	def filt_len(self, length):
	    self.words_df = self.words_df.loc[self.words_df.word.str.len() == length, :]

	# generate distribution of char occurances in dict
	def get_dist(self):
	    return sorted([(k,(self.words_df.word.str.find(k) > -1).mean()) for k in self.keys], key=lambda x: x[1], reverse=True)

	# make guess
	def make_guess(self):
		guess =  self.get_dist()[0][0]
		self.guessed = self.guessed + guess
		self.keys = self.keys - set(self.guessed)
		return guess

	# filter dict after a guess is made
	def filt_guess(self, guess, state):
	    if guess in state: 
	        pattern = ''.join(state).replace('_', f'[^{self.guessed}]')
	        self.words_df = self.words_df.loc[self.words_df.word.str.match(pattern), :]
	    else: self.words_df =  self.words_df.loc[self.words_df.word.str.find(guess) == -1, :]
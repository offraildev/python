import random

# getting a random real number between [0,1)
print(random.random())

# get a random real number between a range
print(random.uniform(1,10))

# get a random integer between a range
print(random.randint(1,10))

# get a random choice of value from a list
colors = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'BLACK']
print(random.choice(colors))

# get a number of random choices from a list
print(random.choices(colors, weights=[0.2,0.2,0.5,0.05,0.05], k=5))

# shuffle a list of numbers
deck = list(range(1,53))  # here the range is generator is not in memory so to shuffle 
random.shuffle(deck)      # it needs to be listed and loaded into memory
print(deck)

# random sample of cards from the deck without repetition
print(random.sample(deck, k=5))

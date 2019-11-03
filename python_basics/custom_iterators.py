# problem split a sentence stirng into words using an iterator 

# class approach: # define input, current index and snapshot
class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence # define input 
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self
    
    def __next__(self):
        current_index = self.index
        if current_index >= len(self.words):
            raise StopIteration
        self.index += 1
        return self.words[current_index]

for word in Sentence('This is a sentence'):
    print(word)

# same thing easier with generators
def sentence(sentence):
    for word in sentence.split():
        yield word


for word in sentence('this is a sentence'):
    print(word)

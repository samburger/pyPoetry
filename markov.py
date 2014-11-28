# coding: utf-8
import random
import collections

corpus = open('testtext.txt', 'r').read()
# Clean the corpus: make all lowercase, remove non-apostrophe symbols & split into list.
corpus = corpus.replace('—', ' ')
corpus = corpus.replace('”', ' ')
corpus = corpus.replace('“', ' ')
corpus = corpus.replace('’', "'")
corpus_words = corpus.lower().translate(None, '.!?@#$-:,;').split()
corpus_words = ['I' if word == 'i' else word for word in corpus_words]


# Function to make weighted choice given list of weights
def weighted_choice(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i


def makePoem(length):
    poem = [random.choice(corpus_words)]
    while len(poem) < length:
        cur_word = poem[-1]
        cur_word_indices = [i for i, x in enumerate(corpus_words) if x == cur_word]
        next_words = [corpus_words[i+1] for i in cur_word_indices if i < len(corpus_words)-1]
        next_words_counter = collections.Counter(next_words)  # Counter used for easy frequency counting.
        new_word = list(next_words_counter.elements())[weighted_choice(list(next_words_counter.values()))]
        poem.append(new_word)
    return ' '.join(poem)

# print the final poem
print makePoem(200)
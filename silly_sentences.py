from random import randint
adjectives = ["Happy", "Sad", "Angry", "Excited", "Bored"]
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
verbs = ["slaps", "climbes", "swims", "kicks", "throws"]
addends = ["a, on a", "the", "my", "your", "their"]
nouns = ["dog", "cat", "car", "house", "tree"]
def pick (words):
 num_words = len(words)
 num_picked = randint(0, num_words - 1)
 word_picked = words[num_picked]
 return word_picked
print(pick(adjectives), pick(names), pick(verbs),pick(addends), pick(nouns), end=".\n")

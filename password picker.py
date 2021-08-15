import random
import string


adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'rad', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'duck', 'panda', 'dog']





adjectives = random.choice(adjectives)
noun = random.choice(nouns)

number = random.randrange(0, 100000)

specil_char = random.choice(string.punctuation)

password = adjectives + noun + str(number) + specil_char
print ('welcome to password picker!')
print('your new password is: %s' % password)

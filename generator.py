#-------------------------------------------------------------------------------
# Name:        Text generator based on Markov chain
# Purpose:
#
# Author:      Andrey Sukhov <suhov.aa@hotmail.com>
#
# Created:     27.09.2023
# Copyright:   (c) Sehktel 2023
# Licence:     MIT Licence
#-------------------------------------------------------------------------------
import json
import random

# Load the probabilities from probabilities.json
with open('probabilities.json', 'r') as f:
    probabilities = json.load(f)

# Define the starting letter and maximum length of the generated text
start_letter = 'п'
words = 16
max_length = 3

# Generate the text
text = start_letter
current_letter = start_letter
for i in range(words):
    if i:
        text+=' '
    for j in range(max_length):
        # Get the probabilities for the current letter
        letter_probabilities = probabilities[current_letter]

        # Choose the next letter based on the probabilities
        next_letter = random.choices(list(letter_probabilities.keys()), list(letter_probabilities.values()))[0]

        # Add the next letter to the text
        text += next_letter

        # Set the current letter to the next letter
        current_letter = next_letter

print(text)
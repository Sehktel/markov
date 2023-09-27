#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Andrew
#
# Created:     26.09.2023
# Copyright:   (c) Andrew 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def main():
    print(generate_markov_chain('lorem_ipsum.txt'))
    pass

if __name__ == '__main__':
    main()

def generate_markov_chain(filename):
    # Read in the text file
    with open(filename, 'r') as f:
        text = f.read()

    # Create a dictionary to store the probabilities
    probs = {}

    # Iterate through the text and count the number of times each symbol appears
    for i in range(len(text)-1):
        curr = text[i]
        next_char = text[i+1]
        if curr not in probs:
            probs[curr] = {}
        if next_char not in probs[curr]:
            probs[curr][next_char] = 0
        probs[curr][next_char] += 1

    # Normalize the probabilities
    for curr in probs:
        total = sum(probs[curr].values())
        for next_char in probs[curr]:
            probs[curr][next_char] /= total

    # Generate the Markov chain
    chain = ''
    curr = random.choice(list(probs.keys()))
    while len(chain) < 100:
        chain += curr
        choices = list(probs[curr].keys())
        weights = list(probs[curr].values())
        curr = random.choices(choices, weights=weights)[0]

    return chain

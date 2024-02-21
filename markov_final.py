#-------------------------------------------------------------------------------
# Name:        Markov chain generator
# Purpose:
#
# Author:      Andrey Sukhov <suhov.aa@hotmail.com>
#
# Created:     27.09.2023
# Copyright:   (c) Sehktel 2023
# Licence:     MIT Licence
#-------------------------------------------------------------------------------
import os
import json

# Define the alphabet to filter symbols
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Create a dictionary to store the symbol counts
symbol_counts = {symbol: {next_symbol: 0 for next_symbol in alphabet}
                    for symbol in alphabet}

# Loop through all txt files in the directory
for filename in os.listdir():
    if filename.endswith('.txt'):
        # Open the file in windows-1251 encoding
        with open(filename, 'r', encoding='windows-1251') as f:
            # Read the file as a string and convert to lowercase
            text = f.read().lower()
            # Filter out non-alphabetic characters and split into a list of symbols
            symbols = [char for char in text if char in alphabet]
            # Count the occurrence of each symbol and add to the dictionary
            for i, symbol in enumerate(symbols):
                if i < len(symbols) - 1:
                    next_symbol = symbols[i+1]
                    symbol_counts[symbol][next_symbol] += 1

# Calculate the total number of symbol pairs
total_pairs = sum([sum(counts.values()) for counts in symbol_counts.values()])

# Calculate the probability of each symbol pair
symbol_probabilities = {symbol: {next_symbol: count/total_pairs for next_symbol, count in counts.items()} for symbol, counts in symbol_counts.items()}

# Save the probabilities as a json file
with open('probabilities.json', 'w') as f:
    json.dump(symbol_probabilities, f)
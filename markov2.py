import os
import json

# Define the alphabet to filter symbols
alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Create a dictionary to store the symbol counts
symbol_counts = {symbol: 0 for symbol in alphabet}

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
            for symbol in symbols:
                symbol_counts[symbol] += 1

# Calculate the total number of symbols
total_symbols = sum(symbol_counts.values())

# Calculate the probability of each symbol appearance
symbol_probabilities = {symbol: count/total_symbols for symbol, count in symbol_counts.items()}

# Save the probabilities as a json file
with open('probabilities.json', 'w') as f:
    json.dump(symbol_probabilities, f)

# Load probabilities.json
with open('probabilities.json', 'r') as f:
    data = json.load(f)

# Print the contents of probabilities.json
print(data)

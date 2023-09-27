import os
import json
import codecs

def clean_text(text):
    # Remove special characters and punctuation marks
    cleaned_text = ''.join(c for c in text if c.isalnum() or c.isspace())
    # Remove extra white spaces
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text

def update_probabilities(prob_dict, current_token, next_token):
    if current_token not in prob_dict:
        prob_dict[current_token] = {}
    if next_token not in prob_dict[current_token]:
        prob_dict[current_token][next_token] = 0
    prob_dict[current_token][next_token] += 1

def normalize_probabilities(prob_dict):
    for current_token in prob_dict:
        total_count = sum(prob_dict[current_token].values())
        for next_token in prob_dict[current_token]:
            prob_dict[current_token][next_token] /= total_count

# Step 1: Create an empty dictionary
prob_dict = {}

# Step 2: Loop through all the text files in the directory
dir_path = './'
for filename in os.listdir(dir_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(dir_path, filename)

        with open(filename, encoding='windows-1251', errors='replace') as f:

        # Open file with UTF-8 encoding
        # with codecs.open(filename, encoding='utf-8') as f:
        # text = f.read()
        #with open(file_path, 'r') as f:
            text = f.read()
            # Step 3: Clean the text
            cleaned_text = clean_text(text)
            # Step 4: Split the text into tokens
            tokens = cleaned_text.split()
            # Step 5: Update the probabilities
            for i in range(len(tokens)-1):
                current_token = tokens[i]
                next_token = tokens[i+1]
                update_probabilities(prob_dict, current_token, next_token)

# Step 6: Normalize the probabilities
normalize_probabilities(prob_dict)

# Step 7: Save the dictionary as a JSON file
with open('probabilities.json', 'w') as f:
    json.dump(prob_dict, f)

# Load probabilities.json
with open('probabilities.json', 'r') as f:
    data = json.load(f)

# Print the contents of probabilities.json
print(data)

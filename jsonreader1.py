#-------------------------------------------------------------------------------
# Name:        jsonreader
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

def beautify_json(json_string, indent=4):
    """Formats a JSON string with indentation for readability."""
    parsed = json.loads(json_string)
    return json.dumps(parsed, indent=indent, ensure_ascii=False)


# Load probabilities.json
with open('probabilities.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Print the contents of probabilities.json
#print(data)

# Convert data to a JSON string and beautify it
json_string = json.dumps(data, ensure_ascii=False)
beautified = beautify_json(json_string)
print(beautified)
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
    return json.dumps(parsed, indent=indent)


# Load probabilities.json
with open('probabilities.json', 'r') as f:
    data = json.load(f)

# Print the contents of probabilities.json
#print(data)

#json_string = '{"name": "John", "age": 30, "city": "New York"}'
beautified = beautify_json(data)
print(beautified)
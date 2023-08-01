
import json
import os

LOGS_PATH = os.path.join(os.path.dirname(__file__), 'logs')
path = os.path.join(LOGS_PATH, 'codefixer', 'gpt-4_0.7_sample3_vote3_greedy1_start0_end3.json')
# Read the JSON file
with open(path, 'r') as file:
    data = json.load(file)

# Iterate over each element in the list
for element in data:
    # Iterate over each step in the element
    step = element['ys']
    # Print the 'ys' field
    text = step[0]
    print(text)  
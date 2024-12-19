import json
import os

DIR = r''
OUT = r''

logs = []

for filename in os.listdir(DIR):
  if 'stripped_' in filename:
    with open(os.path.join(DIR, filename)) as file:
      logs.append(dict(filename = filename, recipe = json.load(file)))
      
for log in logs:
  key = log['recipe']['key']['#']
  result = log['recipe']['result']['id']

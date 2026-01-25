import json
import os
from dotenv import load_dotenv

load_dotenv()

DIR = os.getenv('DIR_PATH')
OUT = os.getenv('VANILLA_OUT_PATH')

if DIR == None or OUT == None:
  print('.env error!')
  exit()

logs = []

for filename in os.listdir(DIR):
  if 'stripped_' in filename and '_wood' in filename:
    with open(os.path.join(DIR, filename)) as file:
      logs.append(dict(filename = filename, recipe = json.load(file)))
      
for log in logs:
  log['recipe']['result']['id'] = log['recipe']['key']['#'].replace('stripped_', '')
  
  with open(os.path.join(OUT, log['filename']), 'w') as file:
    json.dump(log['recipe'], file, indent = 4)

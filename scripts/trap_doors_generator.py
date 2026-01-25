import json
import os
from dotenv import load_dotenv

load_dotenv()

DIR = os.getenv('DIR_PATH')
OUT = os.getenv('VANILLA_OUT_PATH')

if DIR == None or OUT == None:
  print('.env error!')
  exit()

traps = []

for filename in os.listdir(DIR):
  if '_trapdoor' in filename:
    with open(os.path.join(DIR, filename)) as file:
      traps.append(dict(filename = filename, recipe = json.load(file)))

for trap in traps:
  try:
    trap['recipe']['ingredients']
  except:
    trap['recipe']['result']['count'] = 4
  
    with open(os.path.join(OUT, trap['filename']), 'w') as file:
      json.dump(trap['recipe'], file, indent = 4)

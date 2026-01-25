import json
import os
from dotenv import load_dotenv

load_dotenv()

DIR_PATH = os.getenv('DIR_PATH')
OUT_PATH = os.getenv('VANILLA_OUT_PATH')

if DIR_PATH == None or OUT_PATH == None:
  print('.env error!')
  exit()

stairs = []

for filename in os.listdir(DIR_PATH):
  if '_stairs' in filename and '_from' not in filename:
    with open(os.path.join(DIR_PATH, filename)) as file:
      stairs.append(dict(filename = filename, recipe = json.load(file)))

for stair in stairs:
  stair['recipe']['result']['count'] = 7
  
  with open(os.path.join(OUT_PATH, stair['filename']), 'w') as file:
    json.dump(stair['recipe'], file, indent = 4)

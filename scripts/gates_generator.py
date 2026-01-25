import json
import os
from dotenv import load_dotenv

load_dotenv()

DIR_PATH = os.getenv('DIR_PATH')
OUT_PATH = os.getenv('VANILLA_OUT_PATH')

if DIR_PATH == None or OUT_PATH == None:
  print('.env error!')
  exit()

gates = []

for filename in os.listdir(DIR_PATH):
  if '_gate' in filename:
    with open(os.path.join(DIR_PATH, filename)) as file:
      gates.append(dict(filename = filename, recipe = json.load(file)))

for gate in gates:
  gate['recipe']['result']['count'] = 2
  
  with open(os.path.join(OUT_PATH, gate['filename']), 'w') as file:
    json.dump(gate['recipe'], file, indent = 4)

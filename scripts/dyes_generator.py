import json
import os
from dotenv import load_dotenv

load_dotenv()

DIR_PATH = os.getenv('DIR_PATH')
OUT_PATH = os.getenv('VANILLA_OUT_PATH')

if DIR_PATH == None or OUT_PATH == None:
  print('.env error!')
  exit()

dyes = []

for filename in os.listdir(DIR_PATH):
  if '_dye' in filename and 'armor' not in filename:
    with open(os.path.join(DIR_PATH, filename)) as file:
      dyes.append(dict(filename = filename, recipe = json.load(file)))

for dye in dyes:
  try:
    if 'dye' not in [x for x in dye['recipe']['ingredients']][0]:
      # print(dye['recipe']['ingredients'])
      dye['recipe']['result']['count'] = 2
  except:
    pass

for dye in dyes:
  with open(os.path.join(OUT_PATH, dye['filename']), 'w') as file:
    json.dump(dye['recipe'], file, indent = 4)

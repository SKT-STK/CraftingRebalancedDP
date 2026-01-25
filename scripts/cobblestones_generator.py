import json
import os
from dotenv import load_dotenv

load_dotenv()

DIR_PATH = os.getenv('DIR_PATH')
OUT_PATH = os.getenv('VANILLA_OUT_PATH')

if DIR_PATH == None or OUT_PATH == None:
  print('.env error!')
  exit()

cobbles = []

for filename in os.listdir(DIR_PATH):
  with open(os.path.join(DIR_PATH, filename)) as file:
    recipe = json.load(file)
    if recipe['type'] == 'minecraft:crafting_shaped':
      for key in recipe['key']:
        if 'cobblestone' in recipe['key'][key] and 'mossy' not in filename and 'slab' not in filename and 'stairs' not in filename and 'wall' not in filename:
          cobbles.append(dict(filename = filename, recipe = recipe, cobble_key = key))

for cobble in cobbles:
  cobble['recipe']['key'][cobble['cobble_key']] = '#minecraft:stone_crafting_materials'

  with open(os.path.join(OUT_PATH, cobble['filename']), 'w') as file:
    json.dump(cobble['recipe'], file, indent = 4)

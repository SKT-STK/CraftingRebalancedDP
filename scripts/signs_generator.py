import json
import os
from dotenv import load_dotenv

load_dotenv()

CRAFTING_DIR_PATH = os.getenv('DIR_PATH')
CRAFTING_OUT_PATH = os.getenv('VANILLA_OUT_PATH')
LOOT_TABLE_DIR_PATH = os.getenv('LOOT_TABLE_DIR_PATH')
LOOT_TABLE_OUT_PATH = os.getenv('LOOT_TABLE_OUT_PATH')

if CRAFTING_DIR_PATH == None or CRAFTING_OUT_PATH == None or LOOT_TABLE_DIR_PATH == None or LOOT_TABLE_OUT_PATH == None:
  print('.env error!')
  exit()

signs = []

for filename in os.listdir(CRAFTING_DIR_PATH):
  if '_sign' in filename:
    with open(os.path.join(CRAFTING_DIR_PATH, filename)) as file:
      signs.append(dict(filename = filename, recipe = json.load(file)))

for h_sign in [s for s in signs if '_hanging_' in s['filename']]:
  for nh_sign in [s for s in signs if '_hanging_' not in s['filename']]:
    if nh_sign['filename'] == h_sign['filename'].replace('_hanging_', '_'):
      h_sign['recipe']['key']['#'] = nh_sign['recipe']['key']['#']
      
for sign in signs:
  sign['recipe']['result']['count'] = 6
  
  if 'components' not in sign['recipe']['result']:
    sign['recipe']['result']['components'] = {}
  sign['recipe']['result']['components']['minecraft:max_stack_size'] = 64
  
  with open(os.path.join(CRAFTING_OUT_PATH, sign['filename']), 'w') as file:
    json.dump(sign['recipe'], file, indent = 4)

signs = []

for filename in os.listdir(LOOT_TABLE_DIR_PATH):
  if '_sign' in filename:
    with open(os.path.join(LOOT_TABLE_DIR_PATH, filename)) as file:
      signs.append(dict(filename = filename, loot_table = json.load(file)))
      
for sign in signs:
  print(sign['filename'])
  if 'functions' not in sign['loot_table']:
    sign['loot_table']['functions'] = [dict(function = 'minecraft:set_components', components = {})]
  sign['loot_table']['functions'][0]['components']['minecraft:max_stack_size'] = 64
  
  if 'pools' not in sign['loot_table']:
    sign['loot_table']['pools'] = [dict(bonus_rolls = 0.0, rolls = 1.0, conditions = [dict(condition = 'minecraft:survives_explosion')], entries = [dict(type = 'minecraft:item', name = f'minecraft:{sign['filename'].replace('.json', '')}')])]
  
  with open(os.path.join(LOOT_TABLE_OUT_PATH, sign['filename']), 'w') as file:
    json.dump(sign['loot_table'], file, indent = 4)

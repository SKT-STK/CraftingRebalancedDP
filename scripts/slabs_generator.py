import json
import os

DIR_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\.fabric\remappedJars\minecraft-1.21.3-0.16.9\client-intermediary\data\minecraft\recipe'
CRDP_OUT_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\crdp\recipe'
VANILLA_OUT_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\minecraft\recipe'

slabs = []

for filename in os.listdir(DIR_PATH):
  if '_slab' in filename and '_from' not in filename:
    with open(os.path.join(DIR_PATH, filename)) as file:
      slabs.append(dict(filename = filename, recipe = json.load(file)))
      
for slab in slabs:
  result = slab['recipe']['result']['id']
  keys = slab['recipe']['key']['#']
  key: str
  
  if type(keys) is list:
    key = keys[0]
  else:
    key = keys

  slab['recipe']['result']['id'] = key
  slab['recipe']['result']['count'] = 1
  slab['recipe']['key']['#'] = result
  
  slab['recipe']['pattern'] = ['#', '#']
  
  slab['filename'] = f'{key.replace('minecraft:', '')}_from_slabs.json'
  
  with open(os.path.join(CRDP_OUT_PATH, slab['filename']), 'w') as file:
    json.dump(slab['recipe'], file, indent = 4)
    
chiseled = []

for filename in os.listdir(DIR_PATH):
  if 'chiseled_' in filename and 'bookshelf' not in filename and '_from' not in filename:
    with open(os.path.join(DIR_PATH, filename)) as file:
      chiseled.append(dict(filename = filename, recipe = json.load(file)))
      
for recipe in chiseled:
  recipe['recipe']['key']['#'] = recipe['recipe']['key']['#'].replace('_slab', '')
  if recipe['recipe']['key']['#'] == 'minecraft:stone_brick':
    recipe['recipe']['key']['#'] = 'minecraft:stone_bricks'
    
  recipe['recipe']['pattern'] = ['###', '###', '###']
  recipe['recipe']['result']['count'] = 9
  
  with open(os.path.join(VANILLA_OUT_PATH, recipe['filename']), 'w') as file:
    json.dump(recipe['recipe'], file, indent = 4)

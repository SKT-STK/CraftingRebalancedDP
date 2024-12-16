import json
import os

DIR_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\.fabric\remappedJars\minecraft-1.21.3-0.16.9\client-intermediary\data\minecraft\recipe'
OUT_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\minecraft\recipe'

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
    
  print(key)

  slab['recipe']['result']['id'] = key
  slab['recipe']['result']['count'] = 1
  slab['recipe']['key']['#'] = result
  
  slab['recipe']['pattern'] = ['#', '#']
  
  slab['filename'] = f'{key.replace('minecraft:', '')}_from_slabs.json'
  
  with open(os.path.join(OUT_PATH, slab['filename']), 'w') as file:
    json.dump(slab['recipe'], file, indent = 4)

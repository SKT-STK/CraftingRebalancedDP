import json
import os

DIR_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\.fabric\remappedJars\minecraft-1.21.3-0.16.9\client-intermediary\data\minecraft\recipe'
OUT_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\minecraft\recipe'

signs = []

for filename in os.listdir(DIR_PATH):
  if '_sign' in filename:
    with open(os.path.join(DIR_PATH, filename)) as file:
      signs.append(dict(filename = filename, recipe = json.load(file)))

for h_sign in [s for s in signs if '_hanging_' in s['filename']]:
  for nh_sign in [s for s in signs if '_hanging_' not in s['filename']]:
    if nh_sign['filename'] == h_sign['filename'].replace('_hanging_', '_'):
      h_sign['recipe']['key']['#'] = nh_sign['recipe']['key']['#']
      
for sign in signs:
  sign['recipe']['result']['count'] = 6
  
  with open(os.path.join(OUT_PATH, sign['filename']), 'w') as file:
    json.dump(sign['recipe'], file, indent = 4)

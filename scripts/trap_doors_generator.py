import json
import os

DIR = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\.fabric\remappedJars\minecraft-1.21.3-0.16.9\client-intermediary\data\minecraft\recipe'
OUT = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\minecraft\recipe'

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

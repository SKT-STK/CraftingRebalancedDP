import json
import os

DIR = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\.fabric\remappedJars\minecraft-1.21.3-0.16.9\client-intermediary\data\minecraft\recipe'
OUT = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\minecraft\recipe'

logs = []

for filename in os.listdir(DIR):
  if 'stripped_' in filename and '_wood' in filename:
    with open(os.path.join(DIR, filename)) as file:
      logs.append(dict(filename = filename, recipe = json.load(file)))
      
for log in logs:
  log['recipe']['result']['id'] = log['recipe']['key']['#'].replace('stripped_', '')
  
  with open(os.path.join(OUT, log['filename']), 'w') as file:
    json.dump(log['recipe'], file, indent = 4)

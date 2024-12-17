import json
import os

DIR_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\.fabric\remappedJars\minecraft-1.21.3-0.16.9\client-intermediary\data\minecraft\recipe'
OUT_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\minecraft\recipe'

stairs = []

for filename in os.listdir(DIR_PATH):
  if '_stairs' in filename and '_from' not in filename:
    with open(os.path.join(DIR_PATH, filename)) as file:
      stairs.append(dict(filename = filename, recipe = json.load(file)))

for stair in stairs:
  stair['recipe']['result']['count'] = 7
  
  with open(os.path.join(OUT_PATH, stair['filename']), 'w') as file:
    json.dump(stair['recipe'], file, indent = 4)

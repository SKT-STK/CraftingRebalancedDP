import json
import os

DIR_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\.fabric\remappedJars\minecraft-1.21.3-0.16.9\client-intermediary\data\minecraft\recipe'
OUT_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\minecraft\recipe'

gates = []

for filename in os.listdir(DIR_PATH):
  if '_gate' in filename:
    with open(os.path.join(DIR_PATH, filename)) as file:
      gates.append(dict(filename = filename, recipe = json.load(file)))

for gate in gates:
  gate['recipe']['result']['count'] = 2
  
  with open(os.path.join(OUT_PATH, gate['filename']), 'w') as file:
    json.dump(gate['recipe'], file, indent = 4)

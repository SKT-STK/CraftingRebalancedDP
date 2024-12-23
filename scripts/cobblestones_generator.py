import json
import os

DIR_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\.fabric\remappedJars\minecraft-1.21.3-0.16.9\client-intermediary\data\minecraft\recipe'
OUT_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\minecraft\recipe'

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

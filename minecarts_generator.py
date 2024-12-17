import json
import os

DIR_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\.fabric\remappedJars\minecraft-1.21.3-0.16.9\client-intermediary\data\minecraft\recipe'
RECIPE_OUT_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\crdp\recipe'
FUNCTION_OUT_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\crdp\function\crafting'
ADVANCEMENT_OUT_PATH = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\crafting_rebalanced_dp\datapacks\CraftingRebalancedDP\data\crdp\advancement\crafting'

minecarts = []

for filename in os.listdir(DIR_PATH):
  if '_minecart' in filename and '_from' not in filename:
    with open(os.path.join(DIR_PATH, filename)) as file:
      minecarts.append(dict(filename = filename, recipe = json.load(file), advancement = {}, function = {}))
      
for minecart in minecarts:
  ingredient = minecart['recipe']['ingredients'][0]
  result = minecart['recipe']['result']['id']
  
  minecart['recipe']['ingredients'] = [result]
  minecart['recipe']['result']['id'] = ingredient
  
  minecart['advancement'] = dict(
    criteria = dict(
      crafted_from_minecart = dict(
        trigger = 'minecraft:recipe_crafted',
        conditions = dict(
          recipe_id = f'crdp:from_{minecart['filename'].replace('.json', '')}'
        )
      )
    ),
    rewards = dict(
      function = f'crdp:crafting/{minecart['filename'].replace('.json', '')}'
    )
  )
  
  minecart['function'] = f"""advancement revoke @s only crdp:crafting/{minecart['filename'].replace('.json', '')}
give @s minecraft:minecart 1"""
  
  with open(os.path.join(RECIPE_OUT_PATH, f'from_{minecart['filename']}'), 'w') as file:
    json.dump(minecart['recipe'], file, indent = 4)
    
  with open(os.path.join(ADVANCEMENT_OUT_PATH, minecart['filename']), 'w') as file:
    json.dump(minecart['advancement'], file, indent = 4)
    
  with open(os.path.join(FUNCTION_OUT_PATH, minecart['filename'].replace('.json', '.mcfunction')), 'w') as file:
    file.write(minecart['function'])

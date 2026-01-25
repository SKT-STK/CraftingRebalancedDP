import json
import os
from dotenv import load_dotenv

load_dotenv()

DIR_PATH = os.getenv('DIR_PATH')
RECIPE_OUT_PATH = os.getenv('CUSTOM_OUT_PATH')
FUNCTION_OUT_PATH = os.getenv('FUNCTION_OUT')
ADVANCEMENT_OUT_PATH = os.getenv('ADVANCEMENT_OUT')

if DIR_PATH == None or RECIPE_OUT_PATH == None or FUNCTION_OUT_PATH == None or ADVANCEMENT_OUT_PATH == None:
  print('.env error!')
  exit()

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

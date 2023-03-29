import re
import json

file = open("termos_traduzidos.txt", encoding="UTF8")
text = file.read()

dictionary = {}

for line in text.split('\n'):
    match = re.match(r'(\w+)\s@\s(\w+)', line)
    if match:
        term, translation = match.groups()
        dictionary[term] = f"en: {translation}"

# para o value ficar com aspeto de entry de um dicionário: dictionary[term] = f'{{"en": "{translation}"}}'

# print(dictionary)
file.close()

with open('termos_traduzidos.json', 'w', encoding='UTF-8') as out:
    json.dump(dictionary, out, ensure_ascii=False, indent=4)

out.close()

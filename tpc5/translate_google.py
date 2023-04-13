from deep_translator import GoogleTranslator
import json

translator = GoogleTranslator(source='pt', target='en')

file = open("dicionario_medico.json", encoding="UTF8")

dic = json.load(file)

new_dic = {}

for key, value in dic.items():
    # print(translator.translate(key))
    new_dic[key] = {"des": value,
                    "en": translator.translate(key)}

print("Tradução concluída!")

file.close()

with open("dicionario_translation.json") as file:
    json.dump(new_dic, ensure_ascii=False, indent=4)

# tpc - criar dicionario falado usando ficheiro que está no github em vez de googletranslate
# deep translator é muito lento

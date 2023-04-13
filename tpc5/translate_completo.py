from deep_translator import GoogleTranslator
import json
import re

# dicionário médico em json obtido na aula anterior
file = open("dicionario_medico.json", encoding='utf-8')
dic = json.load(file)
file.close()

# remoção das duas primeiras keys do dicionário
del dic["Palavra"]
del dic["Significado"]


# dicionário com alguns termos médicos e traduções em inglês
# criado no ficheiro translate.py
file1 = open("termos_traduzidos.json", encoding='utf-8')
pt_en = json.load(file1)
file1.close()

# criação do novo dicionário com o aspeto: {designação: {"desc": descrição, "en": tradução}}
dic_pt_en = {}
for designation, description in dic.items():
    # linha de código para substituir, nas descrições, todos os carateres que estejam escritos em codigo ASCII pelo respetivo símbolo
    description = re.sub(
        "&#(\d+);", lambda match: chr(int(match.group(1))), description)

    # no caso de a designação estar no dicionário de traduções
    if designation in pt_en.keys():
        dic_pt_en[designation] = {
            "des": description,
            "en": pt_en[designation]
        }

    # no caso de a designação não estar no dicionário de traduções
    else:
        dic_pt_en[designation] = {
            "des": description,
            # demora muito a processar esta parte
            "en": GoogleTranslator(source='pt', target='en').translate(designation)
        }


with open('dicionario_medico_pt_en.json', 'w', encoding='UTF-8') as out:
    json.dump(dic_pt_en, out, ensure_ascii=False, indent=4)

out.close()

import json
import re

# abertura do ficheiro json criado em dicionario_xml.py
dic = open('dicionario_medico.json', encoding='UTF-8')

# para ler um ficheiro json
entries = json.load(dic)
# print(entries)


# FICHEIRO A TRABALHAR
file = open('LIVRO-Doenças-do-Aparelho-Digestivo.txt', encoding='UTF-8')
text = file.read()


# PROCESSAMENTO DO FICHEIRO para posterior escrita em html
# substituição do símbolo de nova página por uma linha horizontal <hr>
text = re.sub(r'\f', f'<hr>', text)
# substituição do símbolo de nova linha por um break <br>
text = re.sub(r'\n', f'<br>', text)


# reconhecimento de termos comuns entre o dicionário e o livro de doenças
# nos termos comuns, colocação de anotação nos mesmos
for designation, description in entries.items():
    matches = re.findall(designation, text, flags=re.IGNORECASE)
    for match in matches:
        text = text.replace(
            match, f'<a href=# title="Definição: {description}">{match}</a>')
# print(text)


# criação do ficheiro html
html = open('livro_doencas_meu.html', 'w', encoding='UTF-8')


header = '''<html>
                <head>
                    <meta charset="UTF-8"/>
                    <title>Livro Doenças Anotado</title>
'''

body = '<h1>Processamento de Linguagem Natural </h1>' + text

footer = '''
                </body>
            </html>
'''

html.write(header + body + footer)


dic.close()
file.close()
html.close()

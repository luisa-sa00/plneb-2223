import re

file = open('dicionario_medico.txt', encoding='UTF-8')
text = file.read()


# mudanças a fazer para ficarem todas as designações/descrições com o mesmo formato (designação \n descrição):
# eliminar \f
# eliminar espaços (\n) a mais

# esta primeira expressão regular apanha os casos casos em que desde o fim da designação até à descrição há 2 \n seguidos de \f, substituindo-os por um só \n
text = re.sub(r'(([^\.])\n\n)\f', r'\2\n', text)
# depois dos casos anteriormente selecionados, esta segunda expressão vai ver onde ainda ficaram \f isolados e simplesmente elimina-os
text = re.sub(r'\f', r'', text)
# esta terceira expressão vai ver um outro caso específico, em que a descrição está separada por um \n a mais, sendo que esse \n separa uma frase completa de outra
text = re.sub(r'(\.)\n\n([A-Z])', r'\1\n\2', text)


# designations = re.findall(r'\n\n.+((\n.+)+)', text)
# findall retorna um tuple com tantos elementos quantos grupos de captura tiver a expressão regular
# neste caso, retorna um tuple com a designação (1º grupo), todas as linhas da descrição (2º grupo), última linha da descrição (3º grupo)
# (.+) -> 1º grupo
# ((\n.+)+) -> 2º grupo
# ((\n.+)) -> 3º grupo
# o que distingue cada grupo por ordem é cada abertura de parêntesis


# para não acontecer o que estava a acontecer, temos de tornar o último grupo de captura apenas um grupo auxiliar, que não retorne output
# porque não queremos que ele retorne a última linha da descrição, queremos que o tuple só tenha 2 elementos: designação, descrição

# antes do grupo de captura que se quer "silenciar", coloca-se ?: dentro do grupo, antes da expressão regular
# de modo a não separar mas sim agrupar o output desse mesmo grupo
entries = re.findall(r'\n\n(.+)((?:\n.+)+)', text)
# print(entries)


# criação de uma nova lista para remover o \n da descrição de cada termo
new_entries = []

for designation, description in entries:
    description = description.strip()
    new_entries.append((designation, description))

# outra maneira de fazer a mesma coisa
new_entries = [(designation, description.strip())
               for designation, description in entries]

# print(new_entries)

file.close()

txt = open('dic_med_alterado.txt', 'w', encoding='UTF-8')
txt.write(text)
txt.close()


# criação do ficheiro html
html = open('dicionario.html', 'w', encoding='UTF-8')

header = '''<html>
                <head>
                    <meta charset="UTF-8"/>
                    <title>Dicionário Médico</title>
                    <style>
                        body {
                            background-color: rgb(20, 40, 60);
                            color: rgb(240, 248, 255);
                            font-family: "Helvetica", "Arial", sans-serif;
                            font-size: 1em;
                            display: flex;
                        }
                        table {
                            width: 70%;
                            justify-self: center;
                            margin-top: 5%;
                        }
                        th, td {
                            height: auto;
                            padding: 10px;
                            border-bottom: 1px solid #ddd;
                        }
                        tr > td:first-child {
                            border-right: 1px solid #ddd;
                        }
                    </style>
                </head>
                <body>
                    <h1>Dicionário Médico</h1>
                    <table>
                           <thead>
                                <tr>
                                    <th><h2>Designação</h2></th>
                                    <th><h2>Descrição</h2></th>
                                </tr>
                            </thead>
                            <tbody>
'''

body = ''
for designation, description in new_entries:
    body += '<tr><td><h3 style="color: #eab676;">' + designation + '</h3></td>'
    body += '<td>' + description + '</td></tr>'

footer = '''
                        </tbody>
                    </table>
                </body>
            </html>
'''

html.write(header + body + footer)

html.close()

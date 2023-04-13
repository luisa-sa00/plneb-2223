Neste trabalho de casa foi usado o ficheiro termos_traduzidos.txt para a criação de um dicionário, guardado em json, com o aspeto seguinte:
{"termo em português": "en: termo em inglês"}.

Para isso, o ficheiro original foi processado, separando-se os termos e as respetivas traduções através do uso de uma expressão regular:
(\w+)\s@\s(\w+) que guarda nos respetivos grupos de captura o termo em português e a sua tradução

Esses grupos de captura são depois utilizados para a criação do dicionário, em que em cada value de cada key é ainda adicionado o prefixo que identifica a língua da tradução, ou seja, "en:".

Depois de conseguido o dicionário, este foi escrito num ficheiro json, como já feito anteriormente.

<b>Atualização:</b>
Na aula nº7, ao ser necessária a utilização do dicionário que tinha ficado para este TPC, percebi que tinha entendido mal o que era o TPC5, pelo que vim atualizar o mesmo. Eu tinha apenas criado um json a partir do ficheiro termos_traduzidos.txt, quando era suposto depois complementar o dicionario_medico.json com este mesmo dicionário de termos traduzidos.

Assim, para este complemento realizei as seguintes tarefas:

- atualizei o ficheiro translate.py, relativo à criação do json a partir do txt de termos traduzidos, para ficar apenas um dicionário com o aspeto: {"termo em português": "termo em inglês"}
- criei o ficheiro translate_completo.py, que utiliza este mesmo dicionário anteriormente mencionado para complementar o dicionario_medico.json do TPC4, criando o ficheiro final, dicionário em json, com o aspeto {designação: {"desc": descrição, "en": tradução}}
- nos casos em que a designação não tinha descrição equivalente no dicionário de termos traduzidos, auxiliei-me do GoogleTranslator do deep_translator para ir buscar a respetiva tradução em falta
- corrigi ainda pequenos erros que já vinham de trás como, por exemplo, o facto de alguns carateres aparecerem na descrição com o respetivo código ASCII e não como símbolo

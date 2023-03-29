Neste trabalho de casa foi usado o ficheiro termos_traduzidos.txt para a criação de um dicionário, guardado em json, com o aspeto seguinte:
{"termo em português": "en: termo em inglês"}.

Para isso, o ficheiro original foi processado, separando-se os termos e as respetivas traduções através do uso de uma expressão regular:
(\w+)\s@\s(\w+) que guarda nos respetivos grupos de captura o termo em português e a sua tradução

Esses grupos de captura são depois utilizados para a criação do dicionário, em que em cada value de cada key é ainda adicionado o prefixo que identifica a língua da tradução, ou seja, "en:".

Depois de conseguido o dicionário, este foi escrito num ficheiro json, como já feito anteriormente.

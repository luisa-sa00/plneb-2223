import requests
import json
from bs4 import BeautifulSoup


# URL principal a trabalhar
url = "https://reference.medscape.com/"

# html da página como texto
html = requests.get(url).text

# BeautifulSoup para o texto passar a ser mesmo HTML
soup = BeautifulSoup(html,"html.parser")

# Div onde começa a listagem dos primeiros links a percorrer
div = soup.find("div", class_="section-content")

# Obtenção dos primeiros urls - Não se trabalham todos da mesma forma, alguns levam até para página de login, portanto não será este o caminho
# alguns url são apêndice do principal outros são urls próprios
hrefs = []
lis = div.ul.find_all("li")
for li in lis:
    hrefs.append(li.a["href"])


# URLs que abrem de formas semelhantes para ir buscar o seu conteúdo
# "https://reference.medscape.com/drugs/XXXXXXX"
# "https://emedicine.medscape.com/clinical_procedures"
# "https://reference.medscape.com/guide/anatomy"
# "https://reference.medscape.com/guide/laboratory_medicine"


dic = {}

# header para os requests mais pesados, para não me recusarem o acesso
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    # "Referer": "https://www.example.com",
    # Add more headers if required
}


#------------------------------------------------ DRUGS ------------------------------------------------

url_drugs = "https://reference.medscape.com/drugs"
html_drugs = requests.get(url_drugs).text
soup_drugs = BeautifulSoup(html_drugs,"html.parser")

# ul onde está a lista de todos os links das drugs
ul = soup_drugs.find("ul", class_="classdruglist")


dic_drugs = {}


lis_drugs = ul.find_all("li")

for li in lis_drugs:
    href = li.a["href"]
    title = li.a.text

    # 1ª camada de urls
    html = requests.get(href).text
    soup = BeautifulSoup(html,"html.parser")

    divs = soup.find_all("div", class_="topic-section")
    
    dic_2 = {}

    # 2ª camada
    for div in divs:
        title_2 = div.find("div", class_="topic-head").text
        
        lis = div.ul.find_all("li")

        #-------------- construção do dicionário "Títulos do dropdown: conteúdo"
        dic_3 = {}
        
        # 3ª camada
        for li in lis:
            href = li.a["href"]
            title_3 = li.a.text

            # TEXTO RELATIVO À ÚLTIMA PÁGINA
            html = requests.get(href, headers = header).text
            # print(html)
            soup = BeautifulSoup(html,"html.parser")

            div = soup.find("div", id="dose_tabs_content")
            if div is not None:
                content = div.text

                dic_3[title_3] = content
        
        #-------------- construção do dicionário secundário "Título principal do dropdown: dicionário 3"
        dic_2[title_2] = dic_3

    #-------------- construção do dicionário "Títulos da lista de Drugs: dicionário 2"
    dic_drugs[title] = dic_2
    
#------------------------------------------------------------------------------------------------------------

with open('tpc9/dicionario_drugs.json', 'w', encoding='UTF-8') as out:
    json.dump(dic_drugs, out, ensure_ascii=False, indent=4)

out.close()


# Atribuição do dicionário das drugs ao dicionário principal
dic["Drugs, OTCs & Herbals"] = dic_drugs


#------------------------------------------- CLINICAL PROCEDURES  -------------------------------------------

url_proc = "https://emedicine.medscape.com/clinical_procedures"
html_proc = requests.get(url_proc).text
soup_proc = BeautifulSoup(html_proc,"html.parser")


dic_proc = {}

divs = soup_proc.find_all("div", class_="topic-section")

for div in divs:
    title = div.find("div", class_="topic-head").text
    
    lis = div.ul.find_all("li")

    #-------------- construção do dicionário "Títulos do dropdown: conteúdo"
    dic_2 = {}
    
    # 2ª camada
    for li in lis:
        href = li.a["href"]
        title_2 = li.a.text

        # TEXTO RELATIVO À ÚLTIMA PÁGINA
        html = requests.get(href, headers = header).text
        # print(html)
        soup = BeautifulSoup(html,"html.parser")

        div = soup.find("div", id="content_a1")
        if div is not None:
            content = div.text

            dic_2[title_2] = content
    
    #-------------- construção do dicionário secundário "Título principal do dropdown: dicionário 3"
    dic_proc[title] = dic_2


#------------------------------------------------------------------------------------------------------------

with open('tpc9/dicionario_proc.json', 'w', encoding='UTF-8') as out:
    json.dump(dic_proc, out, ensure_ascii=False, indent=4)

out.close()


# Atribuição do dicionário das drugs ao dicionário principal
dic["Clinical Procedures"] = dic_proc


#------------------------------------------------- ANATOMY -------------------------------------------------

url_anat = "https://reference.medscape.com/guide/anatomy"
html_anat = requests.get(url_anat).text
soup_anat = BeautifulSoup(html_anat,"html.parser")


dic_anat = {}

divs_2 = soup_proc.find_all("div", class_="topic-section")

for div in divs_2:
    title = div.find("div", class_="topic-head").text
    
    lis = div.ul.find_all("li")

    #-------------- construção do dicionário "Títulos do dropdown: conteúdo"
    dic_2 = {}
    
    # 2ª camada
    for li in lis:
        href = li.a["href"]
        title_2 = li.a.text

        # TEXTO RELATIVO À ÚLTIMA PÁGINA
        html = requests.get(href, headers = header).text
        # print(html)
        soup = BeautifulSoup(html,"html.parser")

        div = soup.find("div", id="content_a1")
        if div is not None:
            content = div.text

            dic_2[title_2] = content
    
    #-------------- construção do dicionário secundário "Título principal do dropdown: dicionário 3"
    dic_anat[title] = dic_2


#------------------------------------------------------------------------------------------------------------

with open('tpc9/dicionario_anat.json', 'w', encoding='UTF-8') as out:
    json.dump(dic_anat, out, ensure_ascii=False, indent=4)

out.close()


# Atribuição do dicionário das drugs ao dicionário principal
dic["Anatomy"] = dic_anat


#------------------------------------------- LABORATORY MEDICINE  -------------------------------------------

url_lab = "https://reference.medscape.com/guide/laboratory_medicine"
html_lab = requests.get(url_lab).text
soup_lab = BeautifulSoup(html_lab,"html.parser")


dic_lab = {}

divs_lab = soup_lab.find_all("div", class_="topic-section")

for div in divs_lab:
    title = div.find("div", class_="topic-head").text
    
    lis = div.ul.find_all("li")

    #-------------- construção do dicionário "Títulos do dropdown: conteúdo"
    dic_2 = {}
    
    # 2ª camada
    for li in lis:
        href = li.a["href"]
        title_2 = li.a.text

        # TEXTO RELATIVO À ÚLTIMA PÁGINA
        html = requests.get(href, headers = header).text
        # print(html)
        soup = BeautifulSoup(html,"html.parser")

        div = soup.find("div", id="content_a1")
        if div is not None:
            content = div.text.strip()

            dic_2[title_2] = content
    
    #-------------- construção do dicionário secundário "Título principal do dropdown: dicionário 3"
    dic_lab[title] = dic_2


#------------------------------------------------------------------------------------------------------------

with open('tpc9/dicionario_lab.json', 'w', encoding='UTF-8') as out:
    json.dump(dic_lab, out, ensure_ascii=False, indent=4)

out.close()


# Atribuição do dicionário das drugs ao dicionário principal
dic["Laboratory Medicine"] = dic_lab



#------------------------------------------- Dicionário principal  -------------------------------------------

# file_drugs = open('tpc9/dicionario_drugs.json', encoding='UTF-8')
# dic_drugs = json.load(file_drugs)
# dic["Drugs, OTCs & Herbals"] = dic_drugs

# file_proc = open('tpc9/dicionario_proc.json', encoding='UTF-8')
# dic_proc = json.load(file_proc)
# dic["Clinical Procedures"] = dic_proc

# file_anat = open('tpc9/dicionario_anat.json', encoding='UTF-8')
# dic_anat = json.load(file_anat)
# dic["Anatomy"] = dic_anat

# file_lab = open('tpc9/dicionario_lab.json', encoding='UTF-8')
# dic_lab = json.load(file_lab)
# dic["Laboratory Medicine"] = dic_lab


with open('tpc9/dicionario_final.json', 'w', encoding='UTF-8') as out:
    json.dump(dic, out, ensure_ascii=False, indent=4)

out.close()

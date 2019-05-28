from bs4 import BeautifulSoup
import requests

def search_google_news(keywords):
    # Generar link de busqueda
    search_url = "https://www.google.com/search?hl=en&gl=us&tbm=nws&authuser=0&q={}".format(keywords.replace(" ", "+"))

    # Efectuar la busqueda y analizar el resultado
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'lxml')

    # Obtener el numero de resultados
    results_number = 0

    try:
        results_element = soup.find("div", {"id": "resultStats"})
        results_text = results_element.findAll(text=True)[0]
        results_text_parts = results_text.split(" ")
        number_part = 0

        if results_text_parts[number_part] == "About":
            number_part = 1

        results_number = int(results_text_parts[number_part].replace(",", ""))
    except:
        pass

    # Obtener los enlaces
    links = list()
    cards = soup.findAll("div", {"class": ["g", "card"]})

    try:
        for card in cards:
            anchor = card.find("a")
            links.append(anchor["href"])
    except:
        pass
    
    return (search_url, results_number, links)

def search_yahoo_news(keywords):
    # Generar link de busqueda
    search_url = "https://news.search.yahoo.com/search?p={}".format(keywords.replace(" ", "+"))

    # Efectuar la busqueda y analizar el resultado
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'lxml')

    # Obtener el numero de resultados
    results_number = 0

    try:
        results_element = soup.find("div", {"class": "compPagination"})
        results_text = results_element.find("span").findAll(text=True)[0]
        results_number = int(results_text.split(" ")[0].replace(",", ""))
    except:
        pass

    # Obtener los enlaces
    links = list()
    cards = soup.findAll("div", {"class": ["dd", "NewsArticle"]})

    try:
        for card in cards:
            anchor = card.find("a")
            links.append(anchor["href"])
    except:
        pass

    return (search_url, results_number, links)
from lxml import html
import requests


def set_joueur1(id_match):
    page = requests.get(id_match)
    tree = html.fromstring(page.content)
    setScore = tree.xpath('//td[contains(@class,"bcen")]/text()')
    result = u""   
    for i in range(0, 5 , 1):
        result+=setScore[i].strip()+" "
    return result

def set_joueur2(id_match):
    page = requests.get(id_match)
    tree = html.fromstring(page.content)
    setScore = tree.xpath('//td[contains(@class,"bcen")]/text()')
    result = u""
    for i in range(5, 10 , 1):
        result+=setScore[i].strip()+" "
    return result


def buteurs_ext(id_match):
    page = requests.get(id_match)
    tree = html.fromstring(page.content)
    buteur_ext = tree.xpath('//td[@class="away"]/span[contains(@class,"slball")]/../text()')
    result = []
    for i in range(0, len(buteur_ext) - 1, 2):
        result.append(" " + buteur_ext[i] + ":" + buteur_ext[i + 1])
    return result


def jaune_ext(id_match):
    page = requests.get(id_match)
    tree = html.fromstring(page.content)
    jaunes = tree.xpath('//td[@class="away"]/span[contains(@class,"yellowcard")]/../text()')
    result = []
    for i in range(0, len(jaunes) - 1, 2):
        result.append(" " + jaunes[i] + ":" + jaunes[i + 1])
    return result


def jaune_home(id_match):
    page = requests.get(id_match)
    tree = html.fromstring(page.content)
    jaunes = tree.xpath('//td[@class="home"]/span[contains(@class,"yellowcard")]/../text()')
    result = []
    for i in range(0, len(jaunes) - 1, 2):
        result.append(jaunes[i + 1] + ":" + jaunes[i])
    return result


def changement_ext(id_match):
    page = requests.get(id_match)
    tree = html.fromstring(page.content)
    chgmt = tree.xpath('//td[@class="away"]/span[contains(@class,"spriteWhite ui-icon-arrow-1-n")]/../text()')
    result = []
    for i in range(0, len(chgmt) - 1, 2):
        result.append(" " + chgmt[i] + "->" + chgmt[i + 1])
    return result


def changement_home(id_match):
    page = requests.get(id_match)
    tree = html.fromstring(page.content)
    chgmt = tree.xpath('//td[@class="home"]/span[contains(@class,"spriteWhite ui-icon-arrow-1-n")]/../text()')
    result = []
    for i in range(0, len(chgmt) - 2, 3):
        result.append(chgmt[i + 1] + "->" + chgmt[i + 2] + " " + chgmt[i])
    return result


def red_ext(id_match):
    page = requests.get(id_match)
    tree = html.fromstring(page.content)
    red = tree.xpath('//td[@class="away"]/span[contains(@class,"redcard")]/../text()')
    jaunejaune = tree.xpath('//td[@class="away"]/span[contains(@class,"second_yellowcard")]/../text()')
    result = []
    for i in range(0, len(red) - 1, 2):
        result.append(red[i] + ":" + red[i + 1])
    for i in range(0, len(jaunejaune) - 1, 2):
        result.append(jaunejaune[i] + ":" + jaunejaune[i + 1])
    return result


def red_home(id_match):
    page = requests.get(id_match)
    tree = html.fromstring(page.content)
    red = tree.xpath('//td[@class="home"]/span[contains(@class,"redcard")]/../text()')
    jaunejaune = tree.xpath('//td[@class="home"]/span[contains(@class,"second_yellowcard")]/../text()')
    result = []
    for i in range(0, len(red) - 1, 2):
        result.append(red[i + 1] + ":" + red[i])
    for i in range(0, len(jaunejaune) - 1, 2):
        result.append(jaunejaune[i + 1] + ":" + jaunejaune[i])
    return result

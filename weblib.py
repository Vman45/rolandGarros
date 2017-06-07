# coding: utf8
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


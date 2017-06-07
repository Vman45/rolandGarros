# coding: utf8
import feedparser
import re
import messagelib
import weblib
import colorlib

regexFeed = '(.*[#])(.*)( [v][s] [#])(.*)([:])(.*)([-])(.*)'
posts = []
url = 'http://www.scorespro.com/rss2/live-tennis.xml'
feed = feedparser.parse(url)
pays1= ''
pays2= ''
joueur1 = ''
sco1 = ''
joueur2 = ''
sco2 = ''
information = ''


def getfeed():
    """Recuperation de l'ensemble du flux et stockage dans la liste des postes"""
    global feed
    global posts
    feed = feedparser.parse(url)
    for i in range(len(feed['entries']) - 1, -1, -1):
        posts.append(feed['entries'][i])            
    return posts

def getdetail(info):
    """Affiche le detail du feed
    :type info: post rss
    """
    joueur1, joueur2, sco1, sco2 = getinfo(info.title)
    detailScore1 = weblib.set_joueur1(info.id)
    detailScore2 = weblib.set_joueur2(info.id)
    print(colorlib.violet(info.id))
    print(colorlib.ecrire(colorlib.ENCRE_JAUNE_VIOLET, info.published))    
    print(colorlib.ecrire(colorlib.ENCRE_BLEU_VIOLET, messagelib.getmessage(info.summary.strip())))    
    print(detailScore1+" "+colorlib.jaune(joueur1+" "+sco1))
    print(detailScore2+" "+colorlib.jaune(joueur2+" "+sco2)) 
    print(" ")
    print(" ")
    
def getinfo(info):
    """Parsing du feed post.summary"""
    match = re.search(regexFeed, info)    
    joueur1 = u""
    joueur2 = u""
    sco1 = u""
    sco2 = u""
    if match:
        joueur1 = match.group(2).strip()
        joueur2 = match.group(4).strip()
        sco1 = match.group(6).strip()
        sco2 = match.group(8).strip()        
    return joueur1, joueur2, sco1, sco2


if __name__ == "__main__":
    listInfo = getfeed()    

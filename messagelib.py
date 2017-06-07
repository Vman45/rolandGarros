# coding: utf8
MSG_SET_UN = u"1st Set"
MSG_SET_DEUX = u"2nd Set"
MSG_SET_TROIS = u"3rd Set"
MSG_SET_QUATRE = u"1st Set"
MSG_SET_CINQ = u"1st Set"
MSG_FIN = u"Match Finished"
MSG_JOUEUR1_OUT = u"P1ret"
MSG_JOUEUR2_OUT = u"P2ret"
MSG_REPORTE = u"Match Postponed"
MSG_PLUIE = u"Rain"

def getmessage(code):
    """Retourne le message correspondant """
    result = code    
    if MSG_SET_UN in code:
        result = u"Premier set"
    elif MSG_SET_DEUX in code:
        result = u"Deuxi\u00e8me set"
    elif MSG_SET_TROIS in code:
        result = u"Troisi\u00e8me set"
    elif MSG_SET_QUATRE in code:
        result = u"Quatri\u00e8me set"
    elif MSG_SET_CINQ in code:
        result = u"Cinqui\u00e8me set"
    elif MSG_FIN in code:
        result = u"Match termin\u00e9"
    elif MSG_REPORTE in code:
        result = u"Match report\u00e9"
    elif MSG_JOUEUR1_OUT in code:
        result = u"Abandon du joueur 1"
    elif MSG_JOUEUR2_OUT in code:
        result = u"Abandon du joueur 2"
    elif MSG_PLUIE in code:
        result = u"Interruption pour cause de pluie"    
    return result

if __name__ == "__main__":
    print (getmessage(MSG_SET_UN))
    print (getmessage(MSG_SET_DEUX))
    print (getmessage(MSG_SET_TROIS))
    print (getmessage(MSG_SET_QUATRE))
    print (getmessage(MSG_SET_CINQ))
    print (getmessage(MSG_FIN))
    print (getmessage(MSG_JOUEUR1_OUT))
    print (getmessage(MSG_JOUEUR2_OUT))
    print (getmessage(MSG_REPORTE) )

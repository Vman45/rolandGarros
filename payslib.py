# coding: utf8
import colorlib
PAYS_ALGERIE = u"ALG"
PAYS_ALLEMAGNE = u"GER"
PAYS_ANGLETERRE = u"ENG"
PAYS_ARABIE = u"KSA"
PAYS_ARGENTINE = u"ARG"
PAYS_AUSTRALIE = u"AUS"
PAYS_AZERBAIDJAN = u"AZE"
PAYS_BANGLADESH = u"BGD"
PAYS_BELGIQUE = u"BEL"
PAYS_BRESIL = u"BRA"
PAYS_COSTA_RICA = u"CRC"
PAYS_COTE_IVOIRE = u"CIV"
PAYS_CHILI = u"CHI"
PAYS_CHYPRE = u"CYP"
PAYS_ECOSSE = u"SCO"
PAYS_EGYPTE = u"EGY"
PAYS_EMIRATS = u"UAE"
PAYS_ESPAGNE = u"ESP"
PAYS_ESTONIE = u"EST"
PAYS_FRANCE = u"FRA"
PAYS_GABON = u"GAB"
PAYS_GALLES = u"WAL"
PAYS_GRECE = u"GRE"
PAYS_GUATEMALA = u"GUA"
PAYS_HONDURAS = u"HON"
PAYS_HONG_KONG = u"HKG"
PAYS_INDE = u"IND"
PAYS_IRAN = u"IRN"
PAYS_IRLANDE = u"NIR"
PAYS_ISLANDE = u"ISL"
PAYS_ISRAEL = u"ISR"
PAYS_ITALIE = u"ITA"
PAYS_JAPON = u"JPN"
PAYS_JORDANIE = u"JOR"
PAYS_KOWEIT = u"KUW"
PAYS_LIBAN = u"LBN"
PAYS_MALTE = u"MLT"
PAYS_MEXIQUE = u"MEX"
PAYS_OMAN = u"OMA"
PAYS_PANAMA = u"PAN"
PAYS_PAYS_BAS = u"NED"
PAYS_PORTUGAL = u"POR"
PAYS_QATAR = u"QAT"
PAYS_SALVADOR = u"SLV"
PAYS_SENEGAL = u"sen"
PAYS_SURINAME = u"SUR"
PAYS_SYRIE = u"SYR"
PAYS_TAHITI = u"TAH"
PAYS_TAIPEI_CHINOIS = u"TPE"
PAYS_TRINITE_TOBAGO = u"TTO"
PAYS_TUNISIE = u"TUN"
PAYS_TURQUIE = u"TUR"
PAYS_VIET_NAM = u"VIE"
MATCH_AMICAL = u"FG"


def getpays(code):
    """Retourne le pays correspondant au code Pays"""
    result = code
    if PAYS_ESPAGNE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Es") + colorlib.ecrire(colorlib.ENCRE_JAUNE, u"pa")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"gne")
    elif PAYS_ITALIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE, u"It") + u"al" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"ie")
    elif PAYS_FRANCE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"Fr") + u"an" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"ce")
    elif PAYS_ANGLETERRE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Ang") + u"let" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"erre")
    elif PAYS_ALLEMAGNE in code:
        result = colorlib.ecrire(colorlib.ENCRE_NOIRE, u"All") + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"ema")
        result += colorlib.ecrire(colorlib.ENCRE_JAUNE, u"gne")
    elif PAYS_PORTUGAL in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE, u"Por") + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"tugal")
    elif PAYS_ALGERIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE, u"Alg")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"\u00e9") + u"rie"
    elif PAYS_ARGENTINE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"Ar") + u"gen" + colorlib.ecrire(colorlib.ENCRE_BLEU, u"tine")
    elif PAYS_GABON in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE, u"Ga") + colorlib.ecrire(colorlib.ENCRE_JAUNE, u"b")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU, u"on")
    elif PAYS_COTE_IVOIRE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ORANGE, u"C\u00f4te") + u" d\u0027iv"
        result += colorlib.ecrire(colorlib.ENCRE_VERTE, u"oire")
    elif PAYS_GRECE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLANC_BLEU, u"Gr")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU_BLANC, u"\u00e8")
        result += colorlib.ecrire(colorlib.ENCRE_BLANC_BLEU, u"ce")
    elif PAYS_JAPON in code:
        result = u"Ja" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"p") + u"on"
    elif PAYS_JORDANIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Jo") + colorlib.ecrire(colorlib.ENCRE_NOIRE, u"rd")
        result += u"an" + colorlib.ecrire(colorlib.ENCRE_VERTE, u"ie")
    elif PAYS_KOWEIT in code:
        result = colorlib.ecrire(colorlib.ENCRE_NOIRE, u"Kow") + colorlib.ecrire(colorlib.ENCRE_VERTE, u"e")
        result += u"\u00ef" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"t")
    elif PAYS_EGYPTE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Eg") + u"yp" + colorlib.ecrire(colorlib.ENCRE_NOIRE, u"te")
    elif PAYS_TAHITI in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Ta") + u"hi" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"ti")
    elif PAYS_BRESIL in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE, u"B") + colorlib.ecrire(colorlib.ENCRE_JAUNE, u"r\u00e9")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU, u"s") + colorlib.ecrire(colorlib.ENCRE_JAUNE, u"i")
        result += colorlib.ecrire(colorlib.ENCRE_VERTE, u"l")
    elif PAYS_SENEGAL in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE, u"S\u00e9") + colorlib.ecrire(colorlib.ENCRE_JAUNE, u"n")
        result += colorlib.ecrire(colorlib.ENCRE_VERTE, u"\u2605 ") + colorlib.ecrire(colorlib.ENCRE_JAUNE, u"g")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"al")
    elif PAYS_TRINITE_TOBAGO in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Trinit\u00e9") + colorlib.ecrire(colorlib.ENCRE_NOIRE, u"et ")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Tobago")
    elif PAYS_SURINAME in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE, u"Su") + u"r"
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"i") + colorlib.ecrire(colorlib.ENCRE_JAUNE, u"\u2605 ")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"n") + u"a" + colorlib.ecrire(colorlib.ENCRE_VERTE, u"me")
    elif PAYS_BANGLADESH in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE, u"Bang") + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"la")
        result += colorlib.ecrire(colorlib.ENCRE_VERTE, u"desh")
    elif PAYS_TUNISIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Tun") + u"i" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"sie")
    elif PAYS_ISRAEL in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"Is") + u"r" + colorlib.ecrire(colorlib.ENCRE_BLEU, u"\u2721")
        result += u" \u00eb" + colorlib.ecrire(colorlib.ENCRE_BLEU, u"l")
    elif PAYS_TURQUIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Tur") + u"q" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"uie")
    elif PAYS_PAYS_BAS in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Pa") + u"ys " + colorlib.ecrire(colorlib.ENCRE_BLEU, u"Bas")
    elif PAYS_IRAN in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE, u"Ir") + u"a" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"n")
    elif PAYS_HONG_KONG in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Hong") + u"\u269d"
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u" Kong")
    elif PAYS_ECOSSE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"\u00c9") + u"c" + colorlib.ecrire(colorlib.ENCRE_BLEU, u"os")
        result += u"s" + colorlib.ecrire(colorlib.ENCRE_BLEU, u"e")
    elif PAYS_GALLES in code:
        result = u"Pays" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"\U0001F432 ")
        result += colorlib.ecrire(colorlib.ENCRE_VERTE, u"Galles")
    elif PAYS_AZERBAIDJAN in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"Azer") + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"ba\u00ef")
        result += colorlib.ecrire(colorlib.ENCRE_VERTE, u"djan")
    elif PAYS_QATAR in code:
        result = u"Qa" + colorlib.ecrire(colorlib.ENCRE_VIOLET, u"tar")
    elif PAYS_BELGIQUE in code:
        result = colorlib.ecrire(colorlib.ENCRE_NOIRE, u"Be") + colorlib.ecrire(colorlib.ENCRE_JAUNE, u"lgi")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"que")
    elif PAYS_AUSTRALIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"A") + u"u" + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"s")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU, u"tralie")
    elif PAYS_ARABIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLANC_VERT, u"Arabie Saoudite")
    elif PAYS_VIET_NAM in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Vi\u00eat") + colorlib.ecrire(colorlib.ENCRE_JAUNE, u"\u2605")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u" Nam")
    elif PAYS_EMIRATS in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Emirats") + colorlib.ecrire(colorlib.ENCRE_VERTE, u" Ara")
        result += u"bes" + colorlib.ecrire(colorlib.ENCRE_NOIRE, u" Unis")
    elif PAYS_IRLANDE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLANC_ROUGE_U, u"Irlande")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE_BLANC, u" du ")
        result += colorlib.ecrire(colorlib.ENCRE_BLANC_ROUGE_U, u"nord")
    elif PAYS_MALTE in code:
        result = u"Mal"+colorlib.ecrire(colorlib.ENCRE_ROUGE, u"te")
    elif PAYS_OMAN in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"O")+colorlib.ecrire(colorlib.ENCRE_BLANC, u"m")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"a") + colorlib.ecrire(colorlib.ENCRE_VERTE, u"n")
    elif PAYS_ESTONIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"Es")
        result += colorlib.ecrire(colorlib.ENCRE_BLANC, u"ton")
        result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"ie")
    elif PAYS_SYRIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Sy")
        result += colorlib.ecrire(colorlib.ENCRE_VERT_BLANC, u"\u2605 r\u2605 ")
        result += colorlib.ecrire(colorlib.ENCRE_BLANC, u"ie")
    elif PAYS_LIBAN in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Li")
        result += colorlib.ecrire(colorlib.ENCRE_VERT_BLANC, u"b\U0001F384 ")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"an")
    elif PAYS_CHYPRE in code:
        result = u"Chy"+colorlib.ecrire(colorlib.ENCRE_ORANGE, u"\U0001F54A ")+u"pre"
    elif PAYS_MEXIQUE in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE, u"Me") + colorlib.ecrire(colorlib.ENCRE_NOIRE, u"x")
        result += colorlib.ecrire(colorlib.ENCRE_ORANGE_BLANC, u"i\U0001F426 ")
        result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"q") + colorlib.ecrire(colorlib.ENCRE_ROUGE, u"ue")
    elif PAYS_COSTA_RICA in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"Co") + colorlib.ecrire(colorlib.ENCRE_BLANC, u"st")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"a ")
        result += colorlib.ecrire(colorlib.ENCRE_BLANC, u"Ri") + colorlib.ecrire(colorlib.ENCRE_BLEU, u"ca")
    elif PAYS_HONDURAS in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"Ho") + colorlib.ecrire(colorlib.ENCRE_NOIRE, u"n")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU_BLANC, u"\u2605\u2605 ")
        result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"d")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU_BLANC, u"\u2605 ") + colorlib.ecrire(colorlib.ENCRE_NOIRE, u"u")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU_BLANC, u"\u2605\u2605 ")
        result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"r") + colorlib.ecrire(colorlib.ENCRE_BLEU, u"as")
    elif PAYS_ISLANDE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"I") + colorlib.ecrire(colorlib.ENCRE_BLANC, u"s")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"l") + colorlib.ecrire(colorlib.ENCRE_BLANC, u"an")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU, u"de")
    elif PAYS_TAIPEI_CHINOIS in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"Ta") + colorlib.ecrire(colorlib.ENCRE_BLANC, u"ip")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"e")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU_BLANC, u"\U0001F338 ")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Chi") + colorlib.ecrire(colorlib.ENCRE_BLANC, u"no")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU, u"is")
    elif PAYS_INDE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ORANGE, u"In")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU_BLANC, u"\U00002638 ")
        result += colorlib.ecrire(colorlib.ENCRE_VERTE, u"de")
    elif PAYS_GUATEMALA in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"Gua")
        result += colorlib.ecrire(colorlib.ENCRE_BLANC, u"tem")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU, u"ala")
    elif PAYS_PANAMA in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU_BLANC, u"\u2605 ")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"Pan")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU, u"ama")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE_BLANC, u"\u2605 ")
    elif PAYS_SALVADOR in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU, u"Sal")
        result += colorlib.ecrire(colorlib.ENCRE_BLANC, u"va")
        result += colorlib.ecrire(colorlib.ENCRE_BLEU, u"dor")
    elif PAYS_CHILI in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLANC_BLEU, u"\u2605 ")
        result += colorlib.ecrire(colorlib.ENCRE_BLANC, u"Ch")
        result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"ili")
    elif MATCH_AMICAL in code:
        result = u"Match Amical"
    return result


if __name__ == "__main__":
    print getpays(u"ESP")
    print getpays(u"ITA")
    print getpays(u"FRA")
    print getpays(u"ENG")
    print getpays(u"GER")
    print getpays(u"POR")
    print getpays(u"ALG")
    print getpays(u"ARG")
    print getpays(u"GAB")
    print getpays(u"CIV")
    print getpays(u"GRE")
    print getpays(u"JPN")
    print getpays(u"JOR")
    print getpays(u"KUW")
    print getpays(u"EGY")
    print getpays(u"TAH")
    print getpays(u"BRA")
    print getpays(u"sen")
    print getpays(u"TTO")
    print getpays(u"SUR")
    print getpays(u"BGD")
    print getpays(u"TUN")
    print getpays(u"ISR")
    print getpays(u"TUR")
    print getpays(u"NED")
    print getpays(u"IRN")
    print getpays(u"HKG")
    print getpays(u"SCO")
    print getpays(u"WAL")
    print getpays(u"AZE")
    print getpays(u"QAT")
    print getpays(u"BEL")
    print getpays(u"AUS")
    print getpays(u"KSA")
    print getpays(u"VIE")
    print getpays(u"UAE")
    print getpays(u"CYP")
    print getpays(u"NIR")
    print getpays(u"MLT")
    print getpays(u"OMA")
    print getpays(u"SYR")
    print getpays(u"LBN")
    print getpays(u"EST")
    print getpays(u"CRC")
    print getpays(u"MEX")
    print getpays(u"HON")
    print getpays(u"ISL")
    print getpays(u"TPE")
    print getpays(u"IND")
    print getpays(u"GUA")
    print getpays(u"SLV")
    print getpays(u"CHI")
    print getpays(u"PAN")
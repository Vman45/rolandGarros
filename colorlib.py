# coding: utf8
ENCRE_ROUGE = [str(1), str(31), str(40)]
ENCRE_VERTE = [str(1), str(32), str(40)]
ENCRE_JAUNE = [str(1), str(33), str(40)]
ENCRE_ORANGE = [str(3), str(30), str(43)]
ENCRE_JAUNE_VIOLET = [str(1), str(33), str(45)]
ENCRE_BLEU_VIOLET = [str(1), str(36), str(45)]
ENCRE_BLANC_BLEU = [str(1), str(37), str(44)]
ENCRE_VERT_BLANC = [str(5), str(32), str(47)]
ENCRE_BLANC_VERT = [str(7), str(32), str(47)]
ENCRE_BLANC = [str(1), str(37), str(40)]
ENCRE_BLEU = [str(1), str(34), str(40)]
ENCRE_VIOLET = [str(1), str(35), str(40)]
ENCRE_NOIRE = [str(7), str(37), str(40)]
ENCRE_BLANC_ROUGE_U = [str(4), str(31), str(47)]
ENCRE_ROUGE_BLANC = [str(7), str(31), str(47)]
ENCRE_NANTES = [str(1), str(33), str(42)]
ENCRE_LORIENT = [str(7), str(30), str(43)]
ENCRE_ORANGE_BLANC = [str(7), str(37), str(43)]
ENCRE_BLEU_BLANC = [str(7), str(37), str(44)]

RED = u"\033[91m"
GREEN = u"\033[1;92m"
YELLOW = u"\033[1;93m"
LIGHT_PURPLE = u"\033[94m"
PURPLE = u"\033[1;95m"
CLIGNOTE = u"\033[25m"
END = u"\033[0m"
BLINK = u"\033[5m"


def liste_couleur():
    print(u"test de couleur")
    print(u"Style, Foreground, Background")
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += "\x1b[%sm %s \x1b[0m" % (format, format)
            print (s1)
        print('\n')
    print("fin test couleur")


def ecrire(couleur, phrase):
    tableau_couleur = ';'.join(couleur)
    return "\x1b[%sm%s\x1b[0m" % (tableau_couleur, phrase)


def clignote(name):
    unicode_string = name.decode('utf-8')
    result = CLIGNOTE+u" {}"+END
    return str(result .format(unicode_string))


def violet(name):
    unicode_string = name.decode('utf-8')
    result = PURPLE+u" {}"+END
    return result .format(unicode_string)


def violet_clair(name):
    unicode_string = name.decode('utf-8')
    result = LIGHT_PURPLE+u" {}"+END
    return str(result .format(unicode_string))


def rouge(name):
    unicode_string = name.decode('utf-8')
    result = RED+u" {}"+END
    return str(result .format(unicode_string))


def vert(name):
    unicode_string = name.decode('utf-8')
    result = GREEN+u" {}"+END
    return str(result .format(unicode_string))


def jaune(name):
    unicode_string = name.decode('utf-8')
    result = YELLOW+u" {}"+END
    return str(result .format(unicode_string))


if __name__ == "__main__":
    liste_couleur()
    print violet("test ecriture violet")
    print violet_clair("test ecriture violet clair")
    print rouge("test ecriture rouge")
    print vert("test ecriture vert")
    print jaune("test ecriture jaune")

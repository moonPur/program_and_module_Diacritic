

import re


def french_diac(text):

    french = re.sub("à|à|â", "a", text)
    french = re.sub("è|ê|ë|é", "e", french)
    french = re.sub("û|ù|ü", "u", french)
    french = re.sub("ô", "o", french)
    french = re.sub("î|ï", "i", french)
    french = re.sub("ÿ", "y", french)
    french = re.sub("ç", "c", french)
    french = re.sub("æ", "ae", french)
    french = re.sub("œ", "oe", french)

    french = re.sub("À|À|Â", "A", french)
    french = re.sub("È|Ê|Ë|É", "E", french)
    french = re.sub("Û|Ù|Ü", "U", french)
    french = re.sub("Ô", "O", french)
    french = re.sub("Î|Ï", "I", french)
    french = re.sub("Ÿ", "Y", french)
    french = re.sub("Ç", "C", french)
    french = re.sub("Æ", "AE", french)
    french = re.sub("Œ", "OE", french)

    return french


def deutsch_diac(text):

    french = re.sub("ä", "ae", text)
    french = re.sub("ö", "oe", french)
    french = re.sub("ü", "ue", french)
    french = re.sub("Ä", "AE", french)
    french = re.sub("Ö", "OE", french)
    french = re.sub("Ü", "UE", french)
    french = re.sub("ß", "ss", french)
    french = re.sub("ẞ", "SS", french)

    return french


def delete_punctuation(text, punctuation):
    str = ''
    for c in text:
        if punctuation.index('\'') > 0 or punctuation.index('–') > 0 or punctuation.index('’') > 0 or punctuation.index('-') > 0:
            if c == '\'' or c == '–' or c == '’' or c == '-':
                c = ' '
        if c not in (punctuation):
            str = str + c

    return str
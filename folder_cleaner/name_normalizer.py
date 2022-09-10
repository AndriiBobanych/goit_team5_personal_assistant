import re


CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ('a', 'b', 'v', 'g', 'd', 'e', 'e', 'j', 'z', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'ts', 'ch',
               'sh', 'sch', '', 'y', '', 'e', 'yu', 'u', 'ja', 'je', 'ji', 'g')

TRANS = {}

for cyrylic, trans in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrylic)] = trans
    TRANS[ord(cyrylic.upper())] = trans.upper()


def translate(file_name: str):
    translate_name = ''
    for char in file_name:
        translate_name += TRANS.get(ord(char), char)
    return translate_name


def normalize(ukr_string: str):
    eng_string = ukr_string.translate(TRANS)
    eng_string = re.sub(r"\W", "_", eng_string)
    return eng_string

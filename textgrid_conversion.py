import tgt
import os
from epitran.flite import Flite


def summarise_textgrids(folder):
    FLITE = Flite()
    phones=[]
    for tg_path in os.listdir(folder):

        textgrid = tgt.io.read_textgrid(folder+"/"+tg_path)

        tier =  textgrid.get_tier_by_name("phones")
        for t in tier._objects:
            p = t.text
            if not(p in phones):
                print(p)
                phones.append(p)

    with open("ipa_phones.txt", 'w', encoding="utf-8") as f:
        f.write(str(phones))


if __name__ == '__main__':
    FLITE = Flite()
    ARPA_IPA = FLITE.arpa_map.values()
    print(ARPA_IPA)
    IPA_to_ARPABET={'ʊ':'OO', 'p':'P', 's':'S', 'spn':'spn', 'd̪':'D', 'ɪ':'IH', 'z':'Z', 'ə':'AX', 'ʎ':'L', 'ɾ':'D', 'ɫ':'L',
                    'm':'M', 'b':'B', 'ɛ':'EH', 'ɹ':'R', 'ŋ':'NG', 'ɐ':'AH', 'ʔ':'Q', 'f':'F', 'ɒ':'AR', 'l':'L', 'pʰ':'P',
                    't':'T', 'kʰ':'K', 'd':'D', 'j':'J', 'ʉː':'UW', 'iː':'IY', 'n':'N', 'tʰ':'T', 'a':'AR', 'k':'K', 'aw':'AW',
                    'ð':'DH', 'aj':'AY', 'ɒː':'AR', 'ɡ':'G', 'ow':'OW', 'h':'H', 'æ':'AE', 'ej':'EY', 'dʲ':'d', 'cʰ':'K', 'ʃ':'SH',
                    'w': 'W', 'dʒ':'J', 'uː':'UW', 'ɟ':'G', 't̪':'T', 'u':'UW', 'mʲ':'M', 'əw':'OW', 'i':'IY', 'ʒ':'ZH', 'ɚ':'ER',
                    'v':'V', 'θ':'TH', 'tʲ':'TH', 'ɲ':'N', 'ɑː':'AR', 'e':'EH', 'ɫ̩':'L', 'ɑ':'AH', 'fʲ':'F', 'cʷ':'K','tʃ':'CH',
                    'c':'K', 'ɜː':'E', 'pʲ':'P', 'ç':'H', 'bʲ':'B', 'ɔ':'OH', 'vʲ':'V', 'ɔj':'OY', 'ʉ':'UW', 'kʷ':'K', 'ɛː':'E',
                    'tʷ':'T', 'ɝ':'ER', 'ɟʷ':'G', 'aː':'AR'}
    ARPABET_TO_IPA ={
        "AA": "ɑ",
        "AE": "æ",
        "AH": "ʌ",
        "AO": "ɔ",
        "AW": "aʊ",
        "AY": "aɪ",
        "EH": "ɛ",
        "ER": "ɜ˞",
        "EY": "eɪ",
        "IH": "ɪ",
        "IX": "ɨ",
        "IY": "i",
        "OW": "oʊ",
        "OY": "ɔɪ",
        "UH": "ʊ",
        "UW": "u",
        "B": "b",
        "CH": "tʃ",
        "D": "d",
        "DH": "ð",
        "F": "f",
        "G": "ɡ",
        "HH": "h",
        "JH": "dʒ",
        "K": "k",
        "L": "l",
        "M": "m",
        "N": "n",
        "NG": "ŋ",
        "P": "p",
        "R": "ɹ",
        "S": "s",
        "SH": "ʃ",
        "T": "t",
        "TH": "θ",
        "V": "v",
        "W": "w",
        "Y": "j",
        "Z": "z",
        "ZH": "ʒ"
    }

    summarise_textgrids("wavs_aligned")
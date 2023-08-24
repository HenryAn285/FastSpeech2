import tgt
from epitran.flite import Flite


def convert_textgrid(dictionary, tg_path):
    FLITE = Flite()

    textgrid = tgt.io.read_textgrid(tg_path)

    tier =  textgrid.get_tier_by_name("phones")
    for t in tier._objects:
        p = t.text
        print(p)
        ipa_p = FLITE.arpa_to_ipa(p)
        print(ipa_p)
    print(tier)

if __name__ == '__main__':
    FLITE = Flite()
    ARPA_IPA = FLITE.arpa_map.values()
    print(ARPA_IPA)
    IPA_to_ARPABET ={
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
    convert_textgrid(IPA_to_ARPABET,"LJSpeech/Textgrid/LJSpeech/LJ001-0001.TextGrid")
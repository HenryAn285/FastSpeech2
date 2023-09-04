import tgt
import os

def check_textgrid(textgrid):
    valid_symbols = [
        "spn",
        "AA",
        "AA0",
        "AA1",
        "AA2",
        "AE",
        "AE0",
        "AE1",
        "AE2",
        "AH",
        "AH0",
        "AH1",
        "AH2",
        "AO",
        "AO0",
        "AO1",
        "AO2",
        "AW",
        "AW0",
        "AW1",
        "AW2",
        "AY",
        "AY0",
        "AY1",
        "AY2",
        "AX",
        "B",
        "CH",
        "D",
        "DH",
        "EH",
        "EH0",
        "EH1",
        "EH2",
        "ER",
        "ER0",
        "ER1",
        "ER2",
        "EY",
        "EY0",
        "EY1",
        "EY2",
        "F",
        "G",
        "HH",
        "IH",
        "IH0",
        "IH1",
        "IH2",
        "IY",
        "IY0",
        "IY1",
        "IY2",
        "JH",
        "K",
        "L",
        "M",
        "N",
        "NG",
        "OW",
        "OW0",
        "OW1",
        "OW2",
        "OY",
        "OY0",
        "OY1",
        "OY2",
        "P",
        "R",
        "S",
        "SH",
        "T",
        "TH",
        "UH",
        "UH0",
        "UH1",
        "UH2",
        "UW",
        "UW0",
        "UW1",
        "UW2",
        "V",
        "W",
        "Y",
        "Z",
        "ZH",
        "OH",
        "OH0",
        "OH1",
        "OH2",
        "IR",
        "IR0",
        "IR1",
        "IR2",
        "AR",
        "AR0",
        "AR1",
        "AR2",
        "UR",
        "UR0",
        "UR1",
        "UR2",
        "Q",
        "J",
        "H"
    ]
    tier = textgrid.get_tier_by_name("phones")

    for t in tier._objects:
        p = t.text
        if not (p in valid_symbols):
            print(p)
            print(tier)
            return False

    return True

def convert_textgrids(dictionary, folder):
    if not os.path.exists("converted/" + folder):
     os.makedirs("converted/" + folder)

    for tg_path in os.listdir(folder):

        textgrid = tgt.io.read_textgrid(folder+"/"+tg_path, include_empty_intervals=True)

        tier =  textgrid.get_tier_by_name("phones")
        for t in tier._objects:
            p = t.text
            new_p = dictionary[p]
            if new_p is 'd':
                new_p = 'D'
                print(new_p)
            #print(new_p)
            t.text=new_p

            #print(t.text)
        #print(tier)
        #with open ("converted/"+folder+"/"+tg_path, "w",encoding="utf-8") as f:
            #f.write(textgrid)
        if not check_textgrid(textgrid):
            print(folder+"/"+tg_path)
            print("false " + new_p)

        tgt.io.write_to_file(textgrid, "converted/"+folder+"/"+tg_path, format='short', encoding='utf-8',)


def summarise_textgrids(folder):
    phones=[]
    for tg_path in os.listdir(folder):

        textgrid = tgt.io.read_textgrid(folder+"/"+tg_path)

        tier =  textgrid.get_tier_by_name("phones")
        for t in tier._objects:
            p = t.text
            if not(p in phones):
                print(p)
                phones.append(p)
        check_textgrid(textgrid)
    with open("ipa_phones.txt", 'w', encoding="utf-8") as f:
        f.write(str(phones))


if __name__ == '__main__':

    IPA_to_ARPABET={'':'spn','ʊ':'UH', 'p':'P', 's':'S', 'spn':'spn', 'd̪':'D', 'ɪ':'IH', 'z':'Z', 'ə':'AX', 'ʎ':'L', 'ɾ':'D', 'ɫ':'L',
                    'm':'M', 'b':'B', 'ɛ':'EH', 'ɹ':'R', 'ŋ':'NG', 'ɐ':'AH', 'ʔ':'Q', 'f':'F', 'ɒ':'AA', 'l':'L', 'pʰ':'P',
                    't':'T', 'kʰ':'K', 'd':'D', 'j':'Y', 'ʉː':'UW', 'iː':'IY', 'n':'N', 'tʰ':'T', 'a':'AR', 'k':'K', 'aw':'AW',
                    'ð':'DH', 'aj':'AY', 'ɒː':'AA', 'ɡ':'G', 'ow':'OW', 'h':'H', 'æ':'AE', 'ej':'EY', 'dʲ':'d', 'cʰ':'K', 'ʃ':'SH',
                    'w': 'W', 'dʒ':'J', 'uː':'UW', 'ɟ':'G', 't̪':'T', 'u':'UW', 'mʲ':'M', 'əw':'OW', 'i':'IY', 'ʒ':'ZH', 'ɚ':'ER',
                    'v':'V', 'θ':'TH', 'tʲ':'TH', 'ɲ':'N', 'ɑː':'AR', 'e':'EH', 'ɫ̩':'L', 'ɑ':'AR', 'fʲ':'F', 'cʷ':'K','tʃ':'CH',
                    'c':'K', 'ɜː':'AX', 'pʲ':'P', 'ç':'H', 'bʲ':'B', 'ɔ':'AO', 'vʲ':'V', 'ɔj':'OY', 'ʉ':'UW', 'kʷ':'K', 'ɛː':'EH',
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

    convert_textgrids(IPA_to_ARPABET,"wavs_aligned")
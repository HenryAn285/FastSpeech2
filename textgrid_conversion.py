import tgt


def convert_textgrid(dictionary, tg_path):
    textgrid = tgt.io.read_textgrid(tg_path)

    tier =  textgrid.get_tier_by_name("phones")
    for t in tier._objects:
        p = t.text
        print(p)
    print(tier)

if __name__ == '__main__':
    IPA_to_ARPABET ={

    }
    convert_textgrid("LJSpeech/Textgrid/LJSpeech/LJ001-0001.TextGrid")
print('test')

def is_vowel(l):
    if l is 'a' or l is 'e' or l is 'i' or l is 'o' or l is 'u':
        return True
    else:
        return False

def process_consonants(syllable):
    simple = ['p', 'b', 'f', 'T', 's', 'z', 'S', 'Z', 't', 'd', '4', 'j', 'k', 'g', 'N', 'h', 'I', 'e', '{', '0', 'U', '6', 'o']

def is_consonant(l):
    consonants = ['p', 'b','m', 'f', 'T', 's', 'z', 'S', 'Z', 't', 'd', '4', 'l', 'n', 'j', 'k', 'g', 'N', 'h']
    if l in consonants:
        return True

def phoneme_convert_en_NZ(phoneme):
    simple = ['p', 'b', 'f', 'v', 'T', 'D', 's', 'z', 'S', 'Z', 't', 'd', '4', 'j', 'k', 'g', 'N', 'h', 'I', 'e', '{', '0', 'U', '6', 'o']
    mapping = {'w':'W', 'p': 'P', 'b': 'B', 'f': 'F', 'v': 'V', 'T': 'TH', 'D': 'DH', 's': 'S', 'z': 'Z', 'S': 'SH', 'Z': 'ZH', 't': 'T', 'd': 'D', '4' : 'DX', 'j': 'Y',
               'k': 'K', 'g': 'G', 'N': 'NG', 'h': 'H', 'n': 'N', 'm': 'M', 'l': 'L',  'r\\': 'R', 'I': 'IH', 'e': 'EH', '{': 'AE', '0': 'OH', 'U': 'UH', '6': 'AH', 'o': 'OW',
               '6:': 'AA', 'i:': 'IY', '{I': 'EY', 'o:': 'AO', '@}': 'OW', '}:': 'UX', 'Ae': 'AY', 'oI': 'OY', '3:': 'ER', '@': 'AX', 'U\\': 'Y UW', 'l=': 'EL',
               'm=': 'EM', 'n=': 'EM', 'I@': 'IR', 'e:': 'IR', }
    vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AX', 'AY', 'IH', 'EH', 'ER',  'EY', 'IR', 'IY', 'OW',  'OY', 'UH', 'UW']
    new_phonemes = ''
    syllables = phoneme.split('-')
    for syllable in syllables:
        new_syllable = ''
        stress = 0
        if syllable.__contains__("\'"):
            stress = 1
        i = 0
        while i < len(syllable):
            new_phoneme = ''
            if i+1 < len(syllable) and syllable[i] + syllable[i+1] in mapping:
                new_phoneme = mapping[syllable[i] + syllable[i + 1]]
                if new_phoneme in vowels:
                    new_phoneme += str(stress)
                new_syllable += new_phoneme + ' '
                i += 1
                #print(syllable[i] + syllable[i+1])
            elif syllable[i] in mapping:
                new_phoneme = mapping[syllable[i]]
                if new_phoneme in vowels:
                    new_phoneme += str(stress)
                new_syllable += new_phoneme + ' '
            i += 1

        #print(syllable)
        #print(new_syllable)
        new_phonemes += new_syllable

    print(new_phonemes)
    return new_phonemes
def convert_en_NZ():
    with open('en_NZ.txt') as lexicon:
        lines = lexicon.readlines()
        output = []
        for line in lines:
            split_line = line.split(' ')
            word = split_line[0]
            print(word)
            if len(split_line) > 1:
                phoneme = split_line[1]
                #print(phoneme)
                new_phoneme = phoneme_convert_en_NZ(phoneme)
                output.append(word + ' ' + new_phoneme)

    #print(output)
    return


convert_en_NZ()


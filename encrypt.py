
def szyfrowanie(text):
    szyfr_dict = {'a': 'y', 'e': 'i', 'i': 'o', 'o': 'a', 'y': 'e'}
    coded = ''
    text = text.lower()
    for letter in text:
        if letter in szyfr_dict.keys():
            coded += szyfr_dict[letter]
        else:
            coded += letter
    return coded


def deszyfrowanie(text):
    deszyfr_dict = {'y': 'a', 'i': 'e', 'o': 'i', 'a': 'o', 'e': 'y'}
    decoded = ''
    text = text.lower()
    for letter in text:
        if letter in deszyfr_dict.keys():
            decoded += deszyfr_dict[letter]
        else:
            decoded += letter
    return decoded

def encrypt(text,key):
    text=text.lower()
    key=key.lower()
    en_text=""
    for x in text:
        en_text+=key[ord(x)-ord('a')]
    return en_text


def dencrypt(text,key):
    text=text.lower()
    key=key.lower()
    key2={}
    for i in range(26):
        key2[key[i]]=chr(ord('a')+i)
    sorted(key2)
    de_text=""
    for x in text:
       de_text+=key2[x]
    return de_text

one=encrypt("hello","phqgiumeaylnofdxjkrcvstzwb")
second=dencrypt(one,"phqgiumeaylnofdxjkrcvstzwb")

print(one,second)
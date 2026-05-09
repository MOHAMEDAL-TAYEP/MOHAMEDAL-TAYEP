def scalekey(key,n):
    key=key.lower()
    scalekey=""
    key_size=len(key)
    for i in range(n):
        scalekey+=key[i%key_size]
    return scalekey


def encrypt(text,key):
    key=scalekey(key,len(text))
    text=text.lower()
    en_text=""
    for  i in range(len(text)):
        x=text[i]
        y=key[i]
        en_text+=(chr((ord(x)+ord(y)-2*ord('a'))%26+ord('a')))
    return en_text


def dencrypt(text,key):
    key=scalekey(key,len(text))
    text=text.lower()
    de_text=""
    for  i in range(len(text)):
        x=text[i]
        y=key[i]
        de_text+=(chr((ord(x)-ord(y)+26)%26+ord('a')))
    return de_text

one=encrypt("hello",'nk')
second=dencrypt(one,'nk')

print(one,second)
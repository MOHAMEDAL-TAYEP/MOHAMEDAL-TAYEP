def encrypt(text,n):
    text=text.lower()
    en_text=""
    for x in text:
        en_text+=(chr((ord(x)-ord('a')+n)%26+ord('a')))
    return en_text


def dencrypt(text,n):
    text=text.lower()
    de_text=""
    for x in text:
        de_text+=(chr((ord(x)-ord('a')-n+26)%26+ord('a')))
    return de_text

one=encrypt("hello",3)
second=dencrypt(one,3)

print(one,second)
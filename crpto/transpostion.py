import math
def encrypt(text,key):
    en_text=""
    k=0
    col= [[char,""] for char in key]
    k=0
    for x in text:
        col[k%len(key)][1]+=x
        k+=1
    col.sort()
    for i in col:
        en_text+=i[1]
    return en_text


def dencrypt(text,key):
    de_text=""
    ln=math.ceil(len(text)/len(key))
    k=0
    size=[]
    for i in key:
        if(len(text)%len(key)>k):
          size.append((i,ln))
        else:
            size.append((i,ln-1))
        k+=1
    k=0
    size.sort()
    texts=[]
    for i in size:
        texts.append(text[k:k+i[1]])
        k+=i[1]
    for j in range(ln):
       for i in key:
          if(len(texts[ord(i)-48])>j):
             de_text+=texts[ord(i)-48][j]
    return de_text
one=encrypt("hello world",'1320')
second=dencrypt(one,'1320')

print(one,second)
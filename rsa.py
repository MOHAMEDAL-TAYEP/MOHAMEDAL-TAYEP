def gcd(a,b):
    while b!=0:
        tmp=b
        b=a%b
        a=tmp
    return a

class needed:
    def __init__(self,p,q):
        self.n=p*q
        self.o=(p-1)*(q-1)
        self.e=1
        for i in range(2,self.n):
            if(gcd(i,self.o)==1):
                self.e=i
                break
        self.d=1 
        for i in range(2,self.o):
            if(i*self.e%self.o==1):
                self.d=i
                break

    
def encrypt(text,p,q):
    l=[]
    text=text.lower()
    num=needed(p,q)
    for x in text:
        l.append(pow(ord(x),num.e,num.n))
    return l

def dencrypt(l,p,q):
    num=needed(p,q)
    de_text=""
    for x in l:
        de_text+=chr(pow(x,num.d,num.n))
    return de_text

one=encrypt("hello",7919,1009)
second=dencrypt(one,7919,1009)

print(one,second)

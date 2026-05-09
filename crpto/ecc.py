import random


def point_add(P, Q, a, mod):
    if P is None: return Q
    if Q is None: return P
    
    x1, y1 = P
    x2, y2 = Q
    
    if x1 == x2 and (y1 != y2 or y1 == 0):
        return None

    if P == Q:
        
        num = (3 * pow(x1, 2, mod) + a) % mod
        den = pow(2 * y1, -1, mod) 
    else:
        
        num = (y2 - y1) % mod
        den = pow(x2 - x1, -1, mod) 

    slope = (num * den) % mod
    
    x3 = (pow(slope, 2, mod) - x1 - x2) % mod
    y3 = (slope * (x1 - x3) - y1) % mod
    
    return (x3, y3)

def point_multiply(k, P, a, mod):
    R = None
    Q = P
    while k > 0:
        if k & 1:
            R = point_add(R, Q, a, mod)
        Q = point_add(Q, Q, a, mod)
        k >>= 1
    return R


def make_keys(G, n, a, p):
    
    d = random.randint(1, n - 1)
    Q = point_multiply(d, G, a, p) 
    return d, Q


def encry(m, Q, G, a, p, n):
    k = random.randint(1, n - 1)
    c1 = point_multiply(k, G, a, p)    
    shared_secret = point_multiply(k, Q, a, p) 
    c2 = point_add(m, shared_secret, a, p)   
    return c1, c2

def decry(c1, c2, d, a, p):
    
    S = point_multiply(d, c1, a, p)
    S_neg = (S[0], (-S[1]) % p)     
    m = point_add(c2, S_neg, a, p)  
    return m

# --- SECP256K1 PARAMETERS ---
a = 0
b = 7
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (Gx, Gy)

# NOTE: For this to work, 'm' MUST be a valid point on the curve.
# Real apps use 'Koblitz's Method' to map data to points.
# For demo, we'll use G multiplied by a random scalar to ensure it's a valid point.
m = point_multiply(12345, G, a, p) 

# Execution
d, Q = make_keys(G, n, a, p)
c1, c2 = encry(m, Q, G, a, p, n)

print(f"Original Point: {m}\n")
print(f"Encrypted c1: {c1}\n")
print(f"Encrypted c2: {c2}\n")

decrypted_m = decry(c1, c2, d, a, p)
print(f"Decrypted Point: {decrypted_m}")
print(f"\nMatch: {m == decrypted_m}")
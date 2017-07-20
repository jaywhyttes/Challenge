from re import finditer
from random import randint,randrange
from fractions import gcd
import math

def bitRange(): # gets user input for encryption level
    RSA32 = '1:       32 - Test one'
    RSA64 = '2:       64 - Test two'
    RSA128 = '3:      128 - Default'
    RSA256 = '4:      256 - Fast generation'
    RSA512 = '5:      512 - Weak generation'
    RSA1024 = '6:     1024 - Secure for most applications'
    RSA2048 = '7:     2048 - Recommended minimum'
    RSA4096 = '8:     4096 - Completely secure'
    RSA8192 = '9:     8192 - Slow generating'
    RSA16384 = '10:   16384 - Not recommended\n'
    # a list of the supplied options, user input -1 to find them in this list
    RSA_pkr = [RSA32, RSA64, RSA128, RSA256, RSA512, RSA1024, RSA2048, RSA4096, RSA8192, RSA16384]
    for i in RSA_pkr:
        print(i)
    RSA_lvl = input('Type 1-10 for RSA encryption level.\n> ')
    while True:
        try:
            RSA_lvl = int(RSA_lvl)
            # checking if input fits in range of 1-10
            if RSA_lvl > 10 or RSA_lvl < 1:
                RSA_lvl = input('Use numbers from 1-10.\n> ')
            else:
                break
        except ValueError:
            # checking if input was a number or letter ect
            RSA_lvl = input('Use numbers from 1-10.\n> ')
    RSA_lvl = [int(x.group()) for x in finditer(r'\d+', RSA_pkr[RSA_lvl-1])][1]
    #sets bits to 1
    bits = 1
    #multiplies bits by 2 to raise bit_length until matches input
    while bits.bit_length() < RSA_lvl:
        bits *= 2
    low = bits
    high = low * 2
    #returns input for display and bit lengths to get random primes later
    return [low, high, RSA_lvl]

def isPrime(n, k=10):   #checks n for primality
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def egcd(a, b): # returns d
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def getKey(l,h):  # gets random primes from bit range  
    p = randint(l,h)
    q = randint(l,h)
    while True:
        if p % 2 == 0:
            p += 1
        if isPrime(p) is False:
            p += 2
        else:
            break
    while True:
        if q % 2 == 0:
            q += 1
            
        if isPrime(q) is False:
            q += 2
        else:
            break
    n = p * q # get n from primes
    phi = (p-1) * (q-1) # get phi from primes
    e = 3 # select 3 as e
    gcd, a, b = egcd(e,phi) # get d from egcd function
    while True:
        if b == 0: # checks if b is 1, extend on e of it isn't
            e += 1
            gcd, a, b = egcd(e,phi)
        else:
            break
    d = a # set d from egcd
    if d < 0:
        d+=phi # check d is negative if so add phi to it
    KU = [e,n] # public key
    KR = [d,n] # private key
    return [KU,KR]

def encrypt(m,e,n,l):
    c = pow(m,e,n) # encrypt using public key and message
    print('Encrypting with RSA'+ str(l) + ' : ' + str(c))
    return c

def decrypt(c,d,n):
    m = pow(c,d,n) # decrypt using cypher text and private key
    print('Decryption : ' + str(m))
    return m

def main():# main function, gets input for bit range and creates keys (encrypts and decrypts for examples)
    m = int(input('(MESSAGE) - Enter a number without spaces.\n> '))
    RSA_lvl = bitRange()
    keys = getKey(RSA_lvl[0],RSA_lvl[1])
    c = encrypt(m,keys[0][0],keys[0][1],RSA_lvl[2])
    m = decrypt(c,keys[1][0],keys[1][1])

main()

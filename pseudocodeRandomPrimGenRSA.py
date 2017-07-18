import random

def getInput():
    bit = int(input("Input RSA encryption bit length\n> "))
    while True:
        if isinstance( bit, int):
            break
        else:
            bit = input("Input RSA encryption bit length\nInput integers\n> ")
    return bit


def bitRange(n):
    if not is_power2(n):
        print('number is not power of 2.')
    while True:
        if n <=1:
            n = input("enter a higher number")
        break
            
    bits = 1
    while bits.bit_length() < n:
        bits *= 2
    low = bits
    high = low * 2 - 1
    return [low, high]

def is_power2(num):
    'states if a number is a power of two'
    return num != 0 and ((num & (num - 1)) == 0)

def is_prime(n, k=10):
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
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def RSACompute(p,q):
    n = p*q
    oen = (p-1)*(q-1)
    return [n,oen]

i = getInput()
bits = bitRange(i)

print(bits)

p = random.randint(bits[0],bits[1])
q = random.randint(bits[0],bits[1])

if p % 2 == 0:
    p += 1
if q % 2 == 0:
    q += 1
    
while is_prime(p) is False:
    p += 2
    
while is_prime(q) is False:
    q += 2
    
#q,p,n,phi = getRandomPrime(bits[0],bits[1])
print(p,q)


#randomPrimes = getRandomPrime(bits[0],bits[1])
#print(randomPrimes)

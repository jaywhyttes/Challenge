import random
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

def is_power2(num):

	'states if a number is a power of two'

	return num != 0 and ((num & (num - 1)) == 0)


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

def getRandomPrime(l,h):
    randRange1 = random.randint(l,h)
    randRange2 = random.randint(l,h)
    while True:
        if randRange2 == randRange1:
            randRange2 = random.randint(l,h)
        else:
            break
    while not is_prime(randRange1):
        randRange1 += 1
    while not is_prime(randRange2):
        randRange2 += 1
    #randRange2 = random.randint(l,h)
    
    return [randRange1, randRange2]
    
    
bits = (bitRange(2048))
randomPrimes = (getRandomPrime(bits[0],bits[1]))
#print(randomPrimes[0] * randomPrimes[1])
print(is_prime(randomPrimes[0]))
print(is_prime(randomPrimes[1]))
n = randomPrimes[0] * randomPrimes[1]
print (n)


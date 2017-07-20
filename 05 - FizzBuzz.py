"""
Fizz Buzz is a game where if x is divisible by three we
reply with Fizz, and if x is divisible by five we reply
with Buzz
"""

def fizzBuzz(x):
    s = 1
    while s <= x:
        if s % 3 == 0:
            print('Fizz')
        elif s % 5 == 0:
            print('Buzz')
        else:
            print(s)
        s += 1

fizzBuzz(50)

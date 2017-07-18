# -*- coding: cp1252 -*-

x = ' ¸{Köü%¥ü%¥ü%¥!åô¥ý%¥ºKú¥Õ%¥ºKÄ¥u%¥ºKÅ'
c = []
a = []
for i in x:
    if i in c:
        pass
    else:
        c.append(i)
        a.append(ord(i))
    print(ord(i))
print(c)
print(len(c))

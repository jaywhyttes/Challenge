# -*- coding: utf-8 -*-
#the above allows to print degree symbols
#temperature converter  - Celsius       (C)     #
#                       - Fahrenheit    (F)     #
#by Jason Whyttes       - Kelvin        (K)     #
#                       - Rankine       (R)     #
#################################################
#C > R = (C + 273.15) * (9.0/5.0)              1#
#R > C = (R - 491.67) * (5.0/9.0)              2#
#################################################
#C > F = C * (9.0/5.0) + 32                    3#
#F > C = (F - 32) / (9.0/5.0)                  4#
#################################################
#C > K = C + 273.15                            5#
#K > C = K - 273.15                            6#
#################################################
#F > R = F + 459.67                            7#
#R > F = R - 459.67                            8#
#################################################
#K > R = K * (9.0/5.0)                         9#
#R > K = R * (5.0/9.0)                        10#
#################################################
#F > K = (F + 495.67) * (5.0/9.0)             11#
#K > F = K * (9.0/5.0) - 459.67               12#
#################################################

def formatting():
    # _________________________________________________________
    #| TYPES | (C)elsius | (F)ahrenheit | (K)alvin | (R)ankine |
    #|_______|___________|______________|__________|___________|
    #Convert from - 'C'
    #Invalid type - 
    #        to   - 'F'
    #Types match  - 
    #Temperature  - '100'
    #Use integer  - 
    #
    #Celsius      - 100
    #Fahrenheit   - 212
    #Calculation  - 100 * 9.0/5.0 + 32  
    print(' ' + '_' * 57)
    print('| TYPES | (C)elsius | (F)ahrenheit | (K)alvin | (R)ankine |')
    print('|_______|___________|______________|__________|___________|')

def getValues():
    valCheck = ['C','F','K','R','CELSIUS','FAHRENHEIT','KALVIN','RANKINE']
    userInput = []
    valA = raw_input('Convert from - ').upper()
    valAItem = ''
    valBItem = ''
    while True:
        if valA in valCheck:
            if len(valA) == 1:
                for item in valCheck:
                    if item[0] == valA and len(item) > 1:
                        valAItem = item
            break
        else:
            valA = raw_input('Invalid type - ').upper()
            
    valB = raw_input('        to   - ').upper()
    while True:
        if valB == valA:
            valB = raw_input('Types match  - ').upper()
        elif valB in valCheck:
            if len(valB) == 1:
                for item in valCheck:
                    if item[0] == valB and len(item) > 1:
                        valBItem = item
            break            
        else:
            valB = raw_input('Invalid type - ').upper() 
            
    temp = raw_input('Temperature  - ')
    while True:
        try:
            temp = float(temp)
            break
        except ValueError:
            temp = raw_input('Use integer  - ')
    userInput.extend([valAItem,valBItem,temp])
    return userInput
           
def conversion(valA,valB,temp):
    value = 0
    calculation = ''
    #1/2
    if valA == 'CELSIUS' and valB == 'RANKINE':
        value = (temp + 273.15) * (9.0/5.0)
        calculation = '({} + 273.15) * (9.0/5.0)'.format(temp)
    elif valA == 'RANKINE' and valB == 'CELSIUS':
        value = (temp - 491.67) * (5.0/9.0)
        calculation = '({} - 491.67) * (5.0/9.0)'.format(temp)
    #3/4
    elif valA == 'CELSIUS' and valB == 'FAHRENHEIT':
        value = temp * (9.0/5.0) + 32
        calculation = '{} * (9.0/5.0) + 32'.format(temp)
    elif valA == 'FAHRENHEIT' and valB == 'CELSIUS':
        value = (temp - 32) / (9.0/5.0)
        calculation = '({} - 32) / (9.0/5.0)'.format(temp)
    #5/6
    elif valA == 'CELSIUS' and valB == 'KALVIN':
        value = temp + 273.15
        calculation = '{} + 273.15'.format(temp)
    elif valA == 'KALVIN' and valB == 'CELSIUS':
        value = temp - 273.15
        calculation = '{} - 273.15'.format(temp)
    #7/8
    elif valA == 'FAHRENHEIT' and valB == 'RANKINE':
        value = temp + 459.67
        calculation = '{} + 459.67'.format(temp)
    elif valA == 'RANKINE' and valB == 'FAHRENHEIT':
        value = temp - 459.67
        calculation = '{} - 459.67'.format(temp)
    #9/10
    elif valA == 'RANKINE' and valB == 'KALVIN':
        value = temp * (9.0/5.0)
        calculation = '{} * (9.0/5.0)'.format(temp)
    elif valA == 'KALVIN' and valB == 'RANKINE':
        value = temp * (5.0/9.0)
        calculation = '{} * (5.0/9.0)'.format(temp)
    #11/12
    elif valA == 'FAHRENHEIT' and valB == 'KALVIN':
        value = (temp + 459.67) * (5.0/9.0)
        calulation = '({} + 459.67) * (5.0/9.0)'.format(temp)
    elif valA == 'KALVIN' and valB == 'FAHRENHEIT':
        value = temp * (9.0/5.0) - 459.67
        calculation = '{} * (9.0/5.0) - 459.67'.format(temp)
    return value, calculation
    
formatting()
userInput = getValues()
results = (conversion(userInput[0],userInput[1],userInput[2]))
print('_' * 58)
print(userInput[0].capitalize() + ' ' * (13 - len(userInput[0])) + '- ' + str(userInput[2]) + '°'[1])
print(userInput[1].capitalize() + ' ' * (13 - len(userInput[1])) + '- ' + str(results[0]) + '°'[1])
print('Calculation  - ' + results[1])


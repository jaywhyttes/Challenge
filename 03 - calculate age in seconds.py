from calendar import isleap, monthrange
from datetime import *

def getDay(maxDays):
    userInput = raw_input("Ender the day you were born   - ")
    while True:
        try:
            intTest = int(userInput)
            if intTest <=maxDays and intTest >= 0:
                userDay = intTest
                break
            else:
                userInput = raw_input("Please use a valid date       - ")
        except ValueError:
            userInput = raw_input("Please use numbers            - ")
    return userDay

def getMonth(year):
    full = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    short = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    integersv1 = ['1','2','3','4','5','6','7','8','9','10','11','12']
    integersv2 = ['01','02','03','04','05','06','07','08','09']

    userInput = raw_input("Enter the month you were born - ").upper()
    while True:
        if userInput in full:
            break
        elif userInput in short or userInput in integersv1 or userInput in integersv2:
            target = [i for i in [full,short,integersv1,integersv2] if userInput in i]
            pos = target[0].index(userInput)
            userInput = full[pos]
            break
        else:
            userInput = raw_input("Please enter a valid month    - ").upper()
    daysInMonth = monthrange( year, full.index(userInput) + 1 )[1]
    dayNum = full.index(userInput)
    return userInput, daysInMonth, dayNum

def getYear():
    leap = 0
    userInput = raw_input("Enter the year you were born  - ")
    while True:
        try:
            intTest = int(userInput)
            userInput = intTest
            break              
        except ValueError:
            raw_input("Please use numbers            - ")
    return userInput

def leapyear(year):
    leap = isleap(year)
    return leap

def countSec(year,month,day):
    birthday = date(year,month,day)
    today = date.today()
    deltaTime = today - birthday
    days = deltaTime.days
    seconds = days * 24 * 60 * 60
    return seconds

def intWithCommas(x):
    if type(x) not in [type(0), type(0L)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)

year = getYear()
leap = leapyear(year)
month = getMonth(2016)
day = getDay(month[1])
seconds = countSec(int(year),int(month[2]),int(day))
timeInSeconds = intWithCommas(seconds)
print(day)
print(month[0].capitalize())
print(year)
print('leap years - ' + str(leap))
print('not calculating leap years currently, results will be off by a little bit.')
print('You have been alive for ' + timeInSeconds + ' seconds.')

##############################################
#             by Jason Whyttes               #
#  this script will calculate the users age  #
#    in seconds and factor in leap years     #
#                                            #
#   -----------How old are you?-----------   #
#                                            #
#   Enter day you were born     -            #
#   Enter month you were born   -            #
#   Enter year you were born    -            #
#   Please use numbers          -            #
#                                            #
#   What time were you born     -            #
#                                            #
#   You have been alive for     - ""seconds  #
#                                            #
#   Check for leap years                     #
#   Get system date and time                 #
#   Get total days since birtday             #
#   Check time format 24 hr or not           #
#   If time is over 12:59 (eg 13:00)         #
#   Use 24 hour time and dont ask for AM/PM  #
#   Else as for AM or PM                     #
##############################################
from time import gmtime, strftime
from calendar import isleap
#use above function to get leap year otherwise
#use year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 )
#   ^first term         ^second and third term first
#works on premis of
#1 - year evenly div by 4           (yes = 2, no = 5)
#2 - year evenly div by 100         (yes = 3, no = 4)
#3 - year evenly div by 400         (yes = 4, no = 5)
#4 - year has 366 days
#5 - year has 365 days
#we are going to use 24 hour time so we do not need to think about AM/PM conversion later on except on if user enters with AM/PM
curTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

#gets user info for birthday, checks input for type and length, max 31, we will check values later on
def userInfo():
    lstOfMonths['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER','1','2','3','4','5','6','7','8','9','10','11','12','01','02','03','04','05','06','07','08','09','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    print('-----------How old are you?-----------\n\n')
    userDay = raw_input("Enter day you were born     - ")
    while True:
        try:
            toInt = int(userDay)
            if toInt <= 31 and toInt >= 0:
                userDay = toInt
                break
            else:
                userDay = raw_input("Please use a valid date     - ")
        except ValueError:
            userDay = raw_input("Please use numbers          - ")
    userMonth = raw_input("Enter month you were born   - ")
    #while True:
    userYear = raw_input("Enter year you were born    - ")
    print("\n")
    userTime = raw_input("What time were you born     - ")
    print("\n")
    return [userDay,userMonth,userYear,userTime]



userInput = userInfo()
#checks if the input exists in 'history' if not it will re-run the userInfo funciton
def checkDayExists(day,month,year):
    print(userInput)

v = checkDayExists(userInput[0],userInput[1],userInput[2])





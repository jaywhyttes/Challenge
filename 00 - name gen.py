from re import findall
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
import random

firstNameProto = ''

def sex():                      # returns the url extension for males and females
    choice = random.randrange(0,3)
    if choice == 0:
        return '/gender/masculine'
    elif choice == 1:
        return '/gender/feminine'
    else:
        return '/gender/unisex'

def getCountry(url):            # gets a country
    # open connection, grab the page
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    # html parser
    page_soup = soup(page_html, "html.parser")
    # return container name and sorts out country names
    containerName = page_soup.findAll("span",{"class":"heavy"})
    countryName = findall(r'/names/usage/(.*?)">',str(containerName))
    return(countryName[random.randrange(0,len(countryName))])

def pickUrl(sex, country):      # page url
    my_url = '{}{}{}{}'.format('https://www.behindthename.com/names',sex,'/usage/',country)
    return my_url

def findNumPages(url):          # check the url to see if there are multiple pages
    # a reference to the current url to use when finding values for the number of pages
    # eg:value="/names/usage/english/13">page 13</option></select>
    container_page_ref = (url[30:]) + '/'
    # open connection, grab the page
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    # html parser
    page_soup = soup(page_html, "html.parser")
    # grabes each item and finds the largest number
    containersPage = str(page_soup.find("select",{"name": "page"}))
    page_num = findall(r'{0}(.*?)">page '.format(container_page_ref), containersPage)
    #checks len of list before conversion to integers
    if len(page_num) > 0:
        page_num_max = (max(map (int, page_num)))
        return page_num_max
    else:
        return ''

def findRandPage(pages):        # return a random number for the page if there are multiple pages
    if pages == '' or pages < 2:
        return my_url
    else:
        return my_url + '/' + str(random.randrange(2, urlPages + 1))

def firstNameLst(url):          # returns a list of first names
    # open connection, grab the page
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    # html parser
    page_soup = soup(page_html, "html.parser")
    # grabs each item in the class called browsename
    # searches out the names and creates a list we can use to draw from randomly
    containersName = page_soup.findAll("div",{"class":"browsename"})
    to_string_name = ''
    if len(containersName) == 0:
        return ''
    else:
        for items in range(0, len(containersName)):
            to_string_name += str((containersName[items].b.a))
    first_name = findall(r'">(.*?)',to_string_name) 
    return first_name[random.randrange(0, len(first_name)) ]

def checkFirstName(extraStr):   # checks the first name for any extra characters (2) or -2-
    if extraStr[:-1] == '-':
        return extraStr[:-2]
    else:
        return extraStr

def mainFirstName():
    global firstNameProto
    firstNameProto = ''
    while firstNameProto == '':
        global sex
        global country
        global my_url
        global urlPages
        global searchPage
        sex = sex()
        country = getCountry('https://www.behindthename.com/names/list')
        my_url = pickUrl(sex, country)
        urlPages = findNumPages(my_url)
        searchPage = findRandPage(urlPages)
        firstNameProto = firstNameLst(searchPage) # if nothing is found try again
    global firstName
    firstName = checkFirstName(firstNameProto)
    return firstName

#sex = sex()
#print(sex)
#country = getCountry('https://www.behindthename.com/names/list')
#print(country)
#my_url = pickUrl(sex, country)
#print(my_url)
#urlPages = findNumPages(my_url)
#print(urlPages)
#searchPage = findRandPage(urlPages)
#print(searchPage)
#firstNameProto = firstNameLst(searchPage)
#print(firstNameProto)
#firstName = checkFirstName(firstNameProto)
#print(firstName)
randomFirstName = mainFirstName()

print(randomFirstName.capitalize() + ' -' + sex.replace('/',' ') + ' - country : ' + country)
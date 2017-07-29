"""
Version: 1 | Date: 30/07/2017 | Developed: Python 2.7.13
Handman game
Jason Whyttes
"""
from re import findall
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from random import randint
#some initial tests for layout and code functions

#difficulty determins word length
#easy <= 5 letters
#medium >= 5 <= 10 letters
#hard >= 10 letters
#expert 2 words >= 5 letters each
#determined with numbers 0-3, 0 being easy and 3 expert
"""
def getWords():
    url = 'https://www.randomlists.com/random-words'
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containerName = page_soup.findAll("span",{"class":"crux"})
    word = findall(r'">(.*?)<',str(containerName))  
    return word
"""
def genList():
    bigList = ['copper', 'explain', 'ill-fated', 'truck', 'neat', 'unite', 'branch', 'educated', 'tenuous', 'hum', 'decisive', 'notice', 'copper', 'explain', 'ill-fated', 'truck', 'neat', 'unite', 'branch', 'educated', 'tenuous', 'hum', 'decisive', 'notice', 'copper', 'explain', 'ill-fated', 'truck', 'neat', 'unite', 'branch', 'educated', 'tenuous', 'hum', 'decisive', 'notice', 'copper', 'explain', 'ill-fated', 'truck', 'neat', 'unite', 'branch', 'educated', 'tenuous', 'hum', 'decisive', 'notice', 'copper', 'explain', 'ill-fated', 'truck', 'neat', 'unite', 'branch', 'educated', 'tenuous', 'hum', 'decisive', 'notice']
    # The scrapping works so we will give the server a break for now and
    # use this list I created from the previous scrape
    """
    while True:
        if len(bigList) < 50:
            for words in getWords():
                bigList.append(words)
        else:
            break
    """
    return bigList
    
def genEasy(words):
    easyWords = []
    for word in words:
        if len(word) < 6:
            easyWords.append(word)
    word = easyWords[randint(0, len(easyWords))]
    return word

def genMedium(words):
    medWords = []
    for word in words:
        if len(word) > 4 and len(word) < 10:
            medWords.append(word)
    word = medWords[randint(0, len(medWords))]
    return word
def genHard(words):
    hardWords = []
    for words in words:
        if len(words) > 9:
            hardWords.append(words)
    word = hardWords[randint(0, len(hardWords))]
    return word

print(genHard(genList()))
#getWords()

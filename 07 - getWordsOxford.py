# Version: 1 | Date: 30/07/2017 | Python 2.7.13
# Scrape the website 'http://www.oxfordlearnersdictionaries.com'
# for words and write to a .txt file for use in our hangman game
# By Jason Whyttes

from re import findall
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

def getWords(url):
    letters = ['A-B/','C-D/','E-G/','H-K/','L-N/','O-P/','Q-R/','S/','T/','U-Z/']
    numPages = [ 5, 7, 6, 4, 4, 5, 3, 5, 3, 3 ]
    p = 0
    wordList = []
    while p < len(numPages):
        for elem in range(1, numPages[p] + 1):
            uClient = uReq(url + letters[p] + '?page=' + str(elem))
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            containerName = page_soup.findAll("ul",{"class":"result-list1 wordlist-oxford3000 list-plain"})
            pageWords = findall(r'definition">(.*?)</a>',str(containerName))
            for item in pageWords:
                wordList.append(item)
        p += 1
    return wordList
    

words = (getWords('http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_'))
newList = []

for s in words:
    if len(s) > 1:
        result = ''.join([i for i in s if not i.isdigit()])
        if result not in newList:
            newList.append(result)
thefile = open('hangmanWords.txt', 'w')
for item in newList:
    thefile.write("%s\n" % item)


# Version: 2 | Date: 30/07/2017 | Python 2.7.13
# Handman game
# By Jason Whyttes

from re import findall
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from random import randint
#some initial tests for layout and code functions

#difficulty determins word length
#easy <= 5 characters
#medium >= 5 <= 10 characters
#hard >= 10 characters

def readData():
    data = open('hangmanWordsData.txt', 'r')
    lines = data.readlines()
    words = []
    for item in lines:
        words.append(item[:-1])
    data.close()
    return words

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

data = readData()
#(genEasy(data))
#(genMedium(data))
#(genHard(data))

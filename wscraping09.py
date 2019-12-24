# LEARNING WEB SCRAPING WITH PYTHON
# Matteo
#
# Getting one random link from a given webpage, following
# the link and doing it again for a set number of times.
# Introducing (Pseudo)Random Number Generators

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re
import datetime
import random


def validateURL(url):
    '''Validates the given URL'''
    try:
        html = urlopen(baseURL + url)
    except URLError:
        return None
    except HTTPError:
        return None
    try:
        bs = BeautifulSoup(html, 'html.parser')
    except AttributeError:
        return None
    else:
        return bs


def getLinks(url):
    '''Gets the list of links found at the given URL'''
    bsObject = validateURL(url)
    urlList = []
    for link in bsObject.find('div', {'id': 'bodyContent'}).findAll(
            'a', href=myRegEx):
        if 'href' in link.attrs:
            urlList.append(link)
    return urlList


def followPrintLinks(url, num):
    '''Gets a link from the given page, prints it, follows it
    and does it again 'num' times'''
    links = getLinks(url)
    while num > 0:
        newLink = links[random.randint(0, len(links)-1)].attrs['href']
        print(newLink)
        num -= 1
        links = getLinks(newLink)


random.seed(datetime.datetime.now())

baseURL = 'http://en.wikipedia.org'
myPage = '/wiki/Kevin_Bacon'
# REGEX: 
# I am targeting ony the links inside a specific 'div' that has
# an ID of 'bodyContent'. Inside this div I am selecting all links
# that start with '/wiki/' and that do not have a ':' character (
# this last part is done by using (?!:))
myRegEx = re.compile('^(/wiki/)((?!:).)*$')
followPrintLinks(myPage, 10)

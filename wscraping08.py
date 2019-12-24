# LEARNING WEB SCRAPING WITH PYTHON
# Matteo
#
# Retrieving a subset of URLs from a single page

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re


def validateURL(url):
    '''Validates the given URL'''
    try:
        html = urlopen(url)
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
    # I am targeting ony the links inside a specific 'div' that has
    # an ID of 'bodyContent'. Inside this div I am selecting all links
    # that start with '/wiki/' and that do not have a ':' character (
    # this last part is done by using (?!:))
    for link in bsObject.find('div', {'id': 'bodyContent'}).findAll(
            'a', href=myRegEx):
        if 'href' in link.attrs:
            urlList.append(link)
    return urlList


def printLinks(lst):
    '''Prints the given list with each item appended to
    its index and with the base Wikipedia URL before the link'''
    i = 1
    for item in lst:
        index = str(i)
        print(index.zfill(3) + '. http://en.wikipedia.org' + item.attrs['href'])
        i += 1


myPage = 'http://en.wikipedia.org/wiki/Kevin_Bacon'
myRegEx = re.compile('^(/wiki/)((?!:).)*$')
myList = getLinks(myPage)
printLinks(myList)

# LEARNING WEB SCRAPING WITH PYTHON
# Matteo
#
# Retrieving all the URLs from a single page

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


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
    for link in bsObject.findAll('a'):
        if 'href' in link.attrs:
            urlList.append(link)
    return urlList


def printLinks(lst):
    '''Prints the given list with each item appended to
    its index'''
    i = 1
    for item in lst:
        index = str(i)
        print(index.zfill(3) + '. ' + item.attrs['href'])
        i += 1


myPage = 'http://en.wikipedia.org/wiki/Kevin_Bacon'
myList = getLinks(myPage)
printLinks(myList)

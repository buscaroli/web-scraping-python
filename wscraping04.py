# LEARNING WEB SCRAPING WITH PYTHON
# Matteo
#
# Checking for Attribute Errors and improving code
# readability by moving part of it into a function

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def getH1(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None
    try:
        bs = BeautifulSoup(html, 'html.parser')
        tag_h1 = bs.body.h1
    except AttributeError:
        return None
    return tag_h1


myPage = 'http://www.pythonscraping.com/pages/page1.html'
h1 = getH1(myPage)
if h1 is None:
    print('No such tag has been found')
else:
    print(h1)

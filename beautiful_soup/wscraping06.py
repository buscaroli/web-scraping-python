# LEARNING WEB SCRAPING WITH PYTHON
# Matteo
#
# Navigating the DOM through the BS object

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def validatedBSObject(url):
    '''Validates a given URL and returns the BS object
    or None'''
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


myPage = 'http://www.pythonscraping.com/pages/page3.html'

bs = validatedBSObject(myPage)
print(8 * '~')
# '''Implemented with a more compact syntax below'''
# giftList = bs.find('', {'id': 'giftList'}).children
# for gift in giftList:
#    print(gift)

# Printing all rows
for child in bs.find('table', {'id': 'giftList'}).children:
    print(6 * '~')
    print(child)

# Printing all rows but the first one
# for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
#     print(sibling)

print(8 * '~')
# Printing the text of the previous sibling of the parent of the image
print(bs.find('img', {'src': '../img/gifts/img4.jpg'}).parent.previous_sibling.getText())
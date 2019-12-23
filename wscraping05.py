# LEARNING WEB SCRAPING WITH PYTHON
# Matteo
#
# Extracting list of names from a web page using findAll
# and a tag.
# the get_text() function strips the tags from the bs object and
# should be done last, after all other operations have been
# performed as it's much easier to find stuff in a beautiful soup
# object rather than in a block of text!!
# Please note thjat with findAll you can also search formore than
# one tag by passing a list e.g. ['h1', 'h2', 'h3']


from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def getNames(url):
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
        nameList = bs.findAll('span', {'class': 'green'})
        return nameList


myPage = 'http://www.pythonscraping.com/pages/warandpeace.html'

print(8 * '~')
nameList = getNames(myPage)
for name in nameList:
    print('- ' + name.getText())

print(8 * '~')
print('Those are the names with no repetitions (list -> set):')
nameSet = set(nameList)
for name in nameSet:
    print('- ' + name.getText())

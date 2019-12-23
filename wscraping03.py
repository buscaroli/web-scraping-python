# LEARNING WEB SCRAPING WITH PYTHON
# Matteo
#
# Checking for URL or HTTP errors

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

print(8 * '~')
print('Trying a working URL:')
try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    bs = BeautifulSoup(html, 'html.parser')
    print(bs.h1)

print(8 * '~')
print('Trying an URL with a wrong server:')
try:
    html2 = urlopen('http://www.py-thon-scra-ping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    bs2 = BeautifulSoup(html2, 'html.parser')
    print(bs2.h1)

print(8 * '~')
print('Trying to access a file that doesn\'t exist:')
try:
    html3 = urlopen('http://www.pythonscraping.com/pages/doesnt-exist.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    bs3 = BeautifulSoup(html3, 'html.parser')
    print(bs3.h1)

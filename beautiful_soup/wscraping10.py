# LEARNING WEBSCRAPING WITH PYTHON
# Matteo
#
# Getting all titles and links from the newspaper 'ilsole24ore.it'
# and printing them to the console.
# TODO Check why only part of the titles/link get saved,
# maybe something is generated on-the-fly (maybe JS ?!?)
# LOOK INTO 'Infinite Loading Pages'

from bs4 import BeautifulSoup
import requests


url = 'http://www.ilsole24ore.com'
titles = []
links = []


response = requests.get(url)
if response.status_code != 200:
    print('Something went wrong. Leaving...')
    quit()
else:
    bs = BeautifulSoup(response.content, 'html.parser')
    articles = bs.findAll(class_='aprev-title')
    # alternative: articles = bs.select('div .aprev-title')

    for article in articles:
        title = article.get_text().strip()
        link = article.find('a', href=True)
        if title is None or link is None:
            print('Missing information: skipping this link...')
        else:
            titles.append(title)
            links.append(link['href'])
            # alternative: links.append(link.get('href'))

    for i in range(1, len(titles)):
        print(str(i).zfill(3) + '.' + titles[i] + '\n' + url + links[i] + '\n')

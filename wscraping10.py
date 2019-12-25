# LEARNING WEBSCRAPING WITH PYTHON
# Matteo
#
# Getting all titles and links from the newspaper 'ilsole24ore.it'
# TODO Check why only part of the titles/link get saved,
# maybe something is generated on-the-fly (maybe JS ?!?)

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
    bs = BeautifulSoup(response.text, 'html.parser')
    articles = bs.findAll(class_='aprev-title')

    for article in articles:
        title = article.get_text()
        link = article.find('a', href=True)
        if title is None or link is None:
            print('Missing information: skipping this link...')
        else:
            titles.append(title)
            links.append(link['href'])
    # print(len(titles))
    # print(len(links))
    for i in range(1, len(titles)):
        print(str(i).zfill(3) + '.' + titles[i] + '\n' + url + links[i] + '\n')


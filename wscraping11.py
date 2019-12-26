# LEARNING WEBSCRAPING WITH PYTHON
# Matteo
#
# Getting all titles and links from the newspaper 'ilsole24ore.it'
# and saving them as a csv file (file name: articles.csv).
# TODO Check why only part of the titles/link get saved,
# maybe something is generated on-the-fly (maybe JS ?!?)
# LOOK INTO 'Infinite Loading Pages'

from bs4 import BeautifulSoup
import requests
import csv


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

    with open('articles.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['TITLE', 'LINK'])
        for article in articles:
            title = article.get_text().strip()
            link = article.find('a', href=True)
            if title is None or link is None:
                print('Missing information: skipping this link...')
            else:
                writer.writerow([title, link])

    # alternative without using 'with'
    # data = csv.writer(open('articles.csv', 'w'))
    # data.writerow(['TITLE', 'LINK'])
    # for article in articles:
    #     title = article.get_text().strip()
    #     link = article.find('a', href=True)
    #     if title is None or link is None:
    #         print('Missing information: skipping this link...')
    #     else:
    #         data.writerow([title, link])

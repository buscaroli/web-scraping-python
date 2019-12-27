# LEARNING WEBSCRAPING WITH PYTHON
# Matteo
#
# Getting Data about the Weather from 'ilmeteo.it'
# Data gets printed to the console with the choice of
# showing the data for the month of for the whole year
# TODO Am I downloading a new soup for every month?
# TODO Maybe create a function that saves the data into
#      a csv file.


from bs4 import BeautifulSoup
import requests


base_url = 'http://ilmeteo.it/portale/archivio-meteo/'


def getPageSoup(url):
    '''Takes an URL, validated it, downloads and
    returns the soup object or None if fails'''
    response = requests.get(url)
    if response.status_code != 200:
        return None
    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        if soup is not None:
            return soup
        else:
            return None


def getSoupByCity(city, year, month):
    '''Takes a city name and year then validates
    and return the URL. Returns None if wrong'''
    url = base_url + city + '/' + year + '/' + '/' + month
    soup = getPageSoup(url)
    if soup is not None:
        return soup
    else:
        return None


def returnTable(city, year, month):
    '''Prints the statistical data for the year'''
    soup = getSoupByCity(city, year, month)
    # removing first unwanted table
    soup.table.decompose()
    soup_table = soup.find('table').findAll('td')
    if soup_table is not None:
        return soup_table
    else:
        return None


def getMonth(city, year, month):
    '''Gets and returns the data for the month'''
    tableSoup = returnTable(city, year, month)
    rows = []
    for item in tableSoup:
        try:
            rows.append(item.get_text().strip())
        except:
            pass
    print(rows[0])
    return rows


def printMonth(city, year, month):
    '''Prints a table with the data of the month to the console'''
    data = getMonth(city, year, month)
    values = ['Day', 'Tmax', 'Tmin', 'Tavg', 'Rain', 'Umidity',
              'Wind max', 'Gust', 'Meteo', 'Other']
    for item in values:
        print(item.ljust(10), end='')
    print('')
    i = 0
    while i < len(data):
        for j in range(10):
            print(data[i].ljust(10, ' '), end='')
            i += 1
        print('')


def printYear(city, year):
    '''Prints a table with the data of the year to the console'''
    months = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile',
              'Maggio', 'Giugno', 'Luglio', 'Agosto',
              'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
    for month in months:
        print(month.center(80, ' '))
        printMonth(city, year, month)


def extractInt(mixed_string):
    '''Takes a string of mixed characters and return the first int value
    or returns None. eg '45 %' becomes '45'.
    Can be used to extract some of the values in the table if more
    convenient to have integers '''
    splLst = mixed_string.split(' ')
    for item in splLst:
        try:
            return int(item)
        except:
            return None


def extractFloat(mixed_string):
    '''Takes a string of mixed characters and return the first int value
    or returns None. eg '45 %' becomes '45'.
    Can be used to extract some of the values in the table if more
    convenient to have integers '''
    splLst = mixed_string.split(' ')
    for item in splLst:
        try:
            return float(item)
        except:
            return None


def printMonthFloat(city, year, month):
    '''Prints a table with the data of the month to the console.
    Data is converted to float where appropriate.'''
    data = getMonth(city, year, month)
    values = ['Day', 'Tmax C', 'Tmin C', 'T avg C', 'Rain mm', 'Umidity %',
              'Wind(Km/h)', 'Gust(Km/h)', 'Meteo', 'Other']
    for item in values:
        print(item.ljust(10), end='')
    print('')
    i = 0
    while i < len(data):
        for j in range(10):
            value = str(extractFloat(data[i]))
            print(value.ljust(10, ' '), end='')
            i += 1
        print('')


def printYearFloat(city, year):
    '''Prints a table with the data of the year to the console.
    Data is converted to float where appropriate.'''
    months = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile',
              'Maggio', 'Giugno', 'Luglio', 'Agosto',
              'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
    for month in months:
        print(month.center(80, ' '))
        printMonthFloat(city, year, month)


# TEST:
# printYear('Livorno', '2019')
# printMonth('Rimini', '2019', 'Gennaio')
printMonthFloat('Rimini', '2019', 'Gennaio')
# printYearFloat('Rimini', '2019')

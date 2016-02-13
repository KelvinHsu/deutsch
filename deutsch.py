#!/home/kelvin/Enthought/Canopy_64bit/User/bin/python
from bs4 import BeautifulSoup
import urllib2
import re

# Functions define
def verbformen(key):
    # Source: http://www.verbformen.de/
    response = urllib2.urlopen('http://www.verbformen.de/konjugation/?i=' + key)
    html = response.read()

    # Navigate to the main article
    parse = BeautifulSoup(html, 'html.parser')
    article = parse.find_all('article', class_='a')
    div = article[0].find_all('div', class_='a')
    sections = div[0].find_all('section')

    # section: steckbrief-formen
    steck = sections[0].find_all('div', id="steckbriefaufzu")
    span = steck[0].find_all('span')
    
    # Extract the wanted data
    delete = re.compile('\xb7')
    tem_0 = span[0].getText()
    tem_1 = span[1].getText()
    tem_2 = span[2].getText()
    string = tem_0 + ', ' + tem_1 + ', ' + tem_2
    result = delete.sub('', string)
    
    return result

# Incomplete  
def verbbedeutung(key):
    # Source: http://www.linguee.com/english-german
    response = urllib2.urlopen('http://www.linguee.com/english-german/search?source=auto&query=' + key)
    html = response.read()
    
    parse = BeautifulSoup(html, 'html.parser')
    mainfield = parse.find_all('div', class_="translation_lines")
    field = mainfield[0].find_all('div', class_='translation featured')
    num = len(field)
    
    
# Main func
keyword = raw_input('Keyword:')
print(verbformen(keyword))
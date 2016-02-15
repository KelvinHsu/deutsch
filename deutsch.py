#!/Users/kelvin/Library/Enthought/Canopy_64bit/User/bin/pythonw
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import re

# Functions define
def verbformen(key):
    # Source: http://www.verbformen.de/
    url = 'http://www.verbformen.de/konjugation/?i={}'.format(key)
    print(url)
    response = urllib2.urlopen(url)
    html = response.read()

    # Navigate to the main article
    parse = BeautifulSoup(html, 'html.parser')
    article = parse.find('article', class_='a')
    div = article.find('div', class_='a')
    sections = div.find_all('section')

    # section: steckbrief-formen
    steck = sections[0].find('div', id="steckbriefaufzu")
    span = steck.find_all('span')
    
    # Extract the wanted data
    delete = re.compile('\xb7|er')
    tem_0 = span[0].getText()
    tem_1 = span[1].getText()
    tem_2 = span[2].getText()
    string = tem_0 + ', ' + tem_1 + ', ' + tem_2
    result = delete.sub('', string)
    
    return result.encode('utf-8')

# Incomplete  
def verbbedeutung(key):
    # Source: http://www.linguee.com/english-german
    url = 'http://www.linguee.com/english-german/search?source=auto&query=' + key
    print url
    response = urllib2.urlopen(url)
    html = response.read()
    
    parse = BeautifulSoup(html, 'html.parser')
    mainfield = parse.find_all('div', class_="translation_lines")
    field = mainfield[0].find_all('div', class_='translation featured')
    
    definitions = []
    for defs in field:
        meanning = defs.find('a', class_='dictLink featured').getText()
        definitions.append(meanning)
    return definitions
    
# Main func
while True:
    #encoding = 'utf-8' if sys.stdin.encoding in (None, 'ascii') else sys.stdin.encoding
    keyword = raw_input('Keyword (type \'exit\' to leave): ')
    keyword = urllib.quote(keyword)
    if keyword == 'exit':
        break
    else:
        print( "({} )".format(verbformen(keyword)) )
        bedeutungen = verbbedeutung(keyword)
        count = 1
        for bedeutung in bedeutungen:
            print("{}. {}".format(count, bedeutung))
            count += 1
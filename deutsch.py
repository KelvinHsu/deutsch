#!/Users/kelvin/Library/Enthought/Canopy_64bit/User/bin/pythonw
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import argparse
import urllib
import urllib2
import re

##### Functions define #####
def readurl(string, key):
    url = string + key
    #print url
    response = urllib2.urlopen(url)
    html = response.read()
    return html

def verbformen(key):
    # Source: http://www.verbformen.de/
    html = readurl('http://www.verbformen.de/konjugation/?i=', key)

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
def bedeutung(key):
    # Source: http://www.linguee.com/english-german
    linguee = 'http://www.linguee.com/english-german/search?source=auto&query='
    html = readurl(linguee, key)
    
    # Navigate to the definition area. Only show common definitions.
    parse = BeautifulSoup(html, 'html.parser')
    mainfield = parse.find_all('div', class_="translation_lines")
    field = mainfield[0].find_all('div', class_='translation featured')
    
    definitions = []
    for defs in field:
        meanning = defs.find('a', class_='dictLink featured').getText()
        definitions.append(meanning)
    return definitions
    
##### Main func #####
# Parsing argument
ap = argparse.ArgumentParser(description='Look up German verbs or nouns.')
ap.add_argument('-v', action='store_const', dest='type',
                const='verb',
                help='Look up verbs')
           
ap.add_argument('-n', action='store_const', dest='type',
                const='noun',
                help='Look up nouns')
                
service = ap.parse_args()
#print 'service = ', service.type

# Looking up words
while True:
    if service.type is None:
        print 'Please specify a flag (-v, or -n).'
        break
    
    #encoding = 'utf-8' if sys.stdin.encoding in (None, 'ascii') else sys.stdin.encoding
    keyword = raw_input('Keyword (type \'exit\' to leave): ')
    keyword = urllib.quote(keyword)
    if keyword == 'exit':
        break
    elif keyword == '':
        continue
    else:
        if service.type == 'verb':
            print( "({} )".format(verbformen(keyword)) )
        elif service.type == 'noun':
            print 'comming soon'
        
        bedeutungen = bedeutung(keyword)
        count = 1
        for term in bedeutungen:
            print("{}. {}".format(count, term))
            count += 1
            
            
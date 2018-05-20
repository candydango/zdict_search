# import libraries
import urllib.request
from urllib.parse   import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
import codecs

# accepts user input 
input_c = input('Input?')
input_d = input_c.encode('utf-8')
input_e = input_d.decode('utf-8')
print('Input:', input_d, input_e)

# specify the url
quote_page = 'http://www.zdic.net/search/?q=' + quote(input_e)

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(quote_page)
print(page.geturl())

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

bpmf_box = soup.find('div', attrs={'class': 'tab-page'})
bpmf = bpmf_box.text.strip()
print(bpmf)

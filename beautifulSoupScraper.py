# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:45:47 2022

@author: ahmad azez rahhal
"""

#Python program to scrape website
#and save quotes from website

# install libraries in python
import requests
from bs4 import BeautifulSoup
import csv

# First of all import the requests library.
# Then, specify the URL of the webpage you want to scrape.
# Send a HTTP request to the specified URL and save the response from server in a response object called r.
# Now, as print r.content to get the raw HTML content of the webpage. It is of ‘string’ type.

#Accessing the HTML content from webpage
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

# we will use html5lib: it is an HTML parsing libraries like lxml, html.parser
#We create a BeautifulSoup object by passing two arguments:
#              r.content : It is the raw HTML content.
#              html5lib : Specifying the HTML parser we want to use.
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())
# soup.prettify() if printed, it gives the visual representation of the parse tree created from the raw HTML content
quotes=[] # a list to store quotes

# find the first div whose id is 'all_quotes'
table = soup.find('div', attrs = {'id':'all_quotes'})
#print(table.prettify())
# now loop on all divs with class attribute 'col-6 ----' and make a dictionary containing the data of a quote then append it to quotes list we mad before
for row in table.findAll('div', attrs = {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
    
# now open a file to put data in it
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['theme','url','img','lines','author'])
	w.writeheader()
	for quote in quotes:
		w.writerow(quote)

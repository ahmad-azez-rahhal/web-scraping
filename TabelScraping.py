# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 09:01:50 2022

@author: ahmad rahhal
"""

# importing modules
import requests
from bs4 import BeautifulSoup
import texttable as tt #To print the data in human-readable format, we will use the library ‘texttable‘

# URL for scrapping data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

data = []

# soup.find_all('td') will scrape every
# element in the url's table
data_iterator = iter(soup.find_all('td'))

# data_iterator is the iterator of the table
# This loop will keep repeating till there is
# data available in the iterator
while True:
	try:
		country = next(data_iterator).text
		confirmed = next(data_iterator).text
		deaths = next(data_iterator).text
		continent = next(data_iterator).text

		# For 'confirmed' and 'deaths',
		# make sure to remove the commas
		# and convert to int
		data.append((
			country,
			int(confirmed.replace(',', '')),
			int(deaths.replace(',', '')),
			continent
		))

	# StopIteration error is raised when
	# there are no more elements left to
	# iterate through
	except StopIteration:
		break

# Sort the data by the number of confirmed cases
data.sort(key = lambda row: row[1], reverse = True)

#To print the data in human-readable format, we will use the library ‘texttable‘

table = tt.Texttable()
 
# Add an empty row at the beginning for the headers
table.add_rows([(None, None, None, None)] + data)
 
# 'l' denotes left, 'c' denotes center,
# and 'r' denotes right
table.set_cols_align(('c', 'c', 'c', 'c')) 
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent '))
 
print(table.draw())
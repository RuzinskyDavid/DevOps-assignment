# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:09:50 2021

@author: ruzin
"""

import requests
from bs4 import BeautifulSoup
import io

url = 'https://www.cts-tradeit.cz/kariera/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

position_tags = soup.findAll('h3', attrs={'class':'card-title mb-0'})
positions = []

print("There are", len(position_tags), "positions available:")
for tag in position_tags:
    positions.append(tag.contents[0][21:].splitlines()[0])
    
for i in range(len(positions)):
    print(i+1, ':', positions[i])

print('e', ':', 'Exit the program')
print('\nTo learn more about them, input their number\n')

options = list(map(str, range(1,len(positions)+1)))
options.append('e')
options.append('E')

for i in range(len(positions)):
    positions[i] = positions[i].replace('/',' ')
    

hyperlink_tags = soup.findAll('a', attrs={'class':'card card-lg card-link-bottom'})
links = []
for i in range(len(hyperlink_tags)):
    links.append(hyperlink_tags[i]['href'][9:])



while True:
    
    user_input = input()
    while user_input not in options:
        print('Wrong input, please select from one of the options', user_input)
        user_input = input()
    
    if (user_input == 'e') or (user_input == 'E'):
        print('Exiting the program')
        break
    
    
    url = 'https://www.cts-tradeit.cz/kariera/' + links[int(user_input)-1]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    
    
    
    p_tags = soup.findAll('p')
    
    childTag = p_tags[2].findAll('span')
    if childTag:
        contents = childTag[0].contents[0]
    else:
        contents = p_tags[2].contents[0]
    
    
    
    
    filename = positions[int(user_input)-1] + '.txt'
    
    with io.open(filename, "w", encoding="utf-8") as f:
        f.write(contents)
    
    print("\nData for selected position have been fetched and saved in txt file\n")
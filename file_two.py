# Aurelio Lopez
# CSS_205
# March 15, 2023

# Task 1 - pip install beautifulsoup4 & pip install lxml

"""
# Task2 - Find a web page which contains at least one image. Use Beautiful Soup to grab the image URL.
from urllib.request import urlopen 
from bs4 import BeautifulSoup

my_site = 'https://www.nps.gov/pinn/index.htm'

site_html=urlopen(my_site)

# create BeautifulSoup object
soup = BeautifulSoup(site_html.read(), 'lxml')

print(soup.title)

# just the text of the title
print(soup.title.text)

# find all images
# can replace 'img' with other html tags
images = soup.findAll('img')
# print(images)

# loop through list of images and retrieve 'src' attribute
for image in images:
    print(image['src'])
"""


from urllib.request import urlopen 
from bs4 import BeautifulSoup
from PIL import Image

from wordcloud import WordCloud, STOPWORDS

my_site = 'https://www.mcsweeneys.net/articles/just-because-im-a-bank-doesnt-mean-im-good-with-money'
site_html=urlopen(my_site)
soup = BeautifulSoup(site_html.read(), 'lxml')

paragraphs = soup.findAll('p')

txt_str = ''
for par in paragraphs:
    txt_str += par.text

wordcloud = WordCloud().generate(txt_str)

image = wordcloud.to_image()
image.show('bank.png')

# I copy this code from instructor. I am trying to understand when I change 'p' to other characer letter in paragraph = soup.findAll('p') it doens't print anything



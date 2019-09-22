import requests
import re
from bs4 import BeautifulSoup

url1 = "http://www.risingupwithsonali.com/feed/" #HEADLINES
url2 = "https://archive.kpft.org/getrss.php?id=risinupsonal" #FULL

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
get_soup1("http://www.risingupwithsonali.com/feed/")
def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
get_soup2("https://archive.kpft.org/getrss.php?id=risinupsonal")

def get_playable_podcast1(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts113/v4/d9/03/20/d9032018-f275-0624-04bf-096bfbada1df/mza_3169664478381694740.jpg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts113/v4/d9/03/20/d9032018-f275-0624-04bf-096bfbada1df/mza_3169664478381694740.jpg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

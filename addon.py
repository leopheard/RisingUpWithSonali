from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "http://www.risingupwithsonali.com/feed/" #HEADLINES
url2 = "https://archive.kpft.org/getrss.php?id=risinupsonal" #FULL
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts113/v4/d9/03/20/d9032018-f275-0624-04bf-096bfbada1df/mza_3169664478381694740.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts113/v4/d9/03/20/d9032018-f275-0624-04bf-096bfbada1df/mza_3169664478381694740.jpg/600x600bb.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup2 = mainaddon.get_soup1(url2)
    playable_podcast = mainaddon.get_playable_podcast(soup2)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()

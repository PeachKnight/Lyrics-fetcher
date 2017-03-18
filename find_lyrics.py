import urllib2
import unicodedata
import requests
from bs4 import BeautifulSoup

def lyrics_fetcher(url):
    """this method takes a lyrics url and \
 makes it text"""
    url_request = requests.get(url)#fetches the url code
    soup = BeautifulSoup(url_request.content, "lxml")#makes the html code look less messy
    lyrics = soup.find_all("p", {"class": "verse"})#searches for the verses in the html code
    empty_list = []

    for item in lyrics:
        empty_list.append(item.text)#cuts more fat from the now unicode
    lyrics_uni = '\n'.join(empty_list)#converts the empty_list into unicode str
    lyrics_str = unicodedata.normalize('NFKD', lyrics_uni).encode('ascii', 'ignore')#transforms the unicode to string
    return lyrics_str

def url_finder():
    """this method takes the song name \
    and generates a URL accordingly"""
    name_of_song = "-".join((raw_input("please enter the name of the song: ")).lower().split())
    name_of_artist = "-".join((raw_input("please enter the name of the artist: ")).lower().split())
    url_get = []
    url_get.append(name_of_song)
    url_get.append(name_of_artist)
    url_get = "-lyrics-".join(url_get)
    url_get = ("http://www.metrolyrics.com/" + url_get.replace(", ", "-") + ".html")
    return url_get


print lyrics_fetcher(url_finder())

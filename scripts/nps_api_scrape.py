import urllib.request
from bs4 import BeautifulSoup
import json
import requests




def makeSoup(webpage):
    '''
    create a beautiful soup object that represents the webpage as a nested data structure
    '''
    soup = BeautifulSoup(webpage.content,"html.parser")
    return soup

def api_scrape():
    '''
    submit request to nps.gov api sequentially to grab all data listed ont the
    nps.gov documentation webpage. webcam data is omitted
    replace INSERT KEY HERE with your own personal access key 
    '''
    key = 'INSERT KEY HERE'
    nps_contents = {}
    content = ['activities','alerts','amenities','articles','campgrounds','events','lessonplans','newsreleases','parks','passportstamplocations','people','places','thingstodo','topics','tours','visitorcenters']
    for i in range(len(content)):
        data = requests.get("https://developer.nps.gov/api/v1/"+content[i]+"?&api_key="+key)
        new_data = json.loads(makeSoup(data).text)
        nps_contents[content[i]] = new_data
    return nps_contents

import requests
import xmltodict
import os


class Zillow(object):
    """A python wrapper for the Zillow Home API"""
    def __init__(self, arg):
        self.ZWSID = os.environ['ZWSID']
        self.base = "https://www.zillow.com/webservice/"

    def GetSearchResults(self, address, citystatezip):
        



data = {'zws-id' : ZWSID,'address' : "3276 Spyglass Drive",'citystatezip':"98226"}

response = requests.get(base + "GetSearchResults.htm",params=data)

house = xmltodict.parse(response.text)

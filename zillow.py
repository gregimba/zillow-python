import requests
import xmltodict
import os


class Zillow(object):
    """A python wrapper for the Zillow Home API"""
    def __init__(self, arg):
        self.ZWSID = os.environ['ZWSID']
        self.base = "https://www.zillow.com/webservice/"

    def GetSearchResults(self, address, citystatezip):

        data = {'zws-id' : self.ZWSID,'address' : address,'citystatezip': citystatezip}

        response = requests.get(base + "GetSearchResults.htm",params=data)
        if response.status_code == 200:
            return xmltodict.parse(response.text)
        else:
            return response.status_code

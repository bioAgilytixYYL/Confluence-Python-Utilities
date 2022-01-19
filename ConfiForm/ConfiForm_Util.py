import requests
from atlassian import Confluence
import time
from getpass import getpass




class ConfiForm_Utils:
    def __init__(self, confluenceBaseUrl, userName, password):
        self.__username = userName
        self.__password = password
        self.__confluenceBaseUrl = confluenceBaseUrl
         
    def getConfiFormEntries(self, pageId, formName):
        requestUrl = "{}/ajax/confiforms/rest/filter.action?pageId={}&f={}".format(self.__confluenceBaseUrl, pageId, formName)
        requestResponse = requests.get(requestUrl, auth=(self.__username, self.__password))

        return requestResponse.json()['list']['entry']

import requests
import time
from atlassian import Confluence
import json
from getpass import getpass

class Confluence_Util:
    def __init__(self, baseUrl, userName, password):
        
        # Change these based on your instance
        self.__confluenceBaseUrl = baseUrl
        self.__contentApiUrl = '/rest/api/'
        self.__username = userName
        self.__password = password
        self.__confluence = Confluence(url=baseUrl,username=userName,password=password)
        
    def get_all_page_id_from_space(self, spaceKey):
        requestUrl = "{}{}space/{}/content?start=0&limit=9999&type=page".format(
            self.__confluenceBaseUrl, self.__contentApiUrl, spaceKey)
        print(requestUrl)

        requestResponse = requests.get(
            requestUrl, auth=(self.__username, self.__password))
        print(requestResponse)
        idList = list()
        for page in requestResponse.json()['page']['results']:
           idList.append(page['id'])
        return idList

    def getAllChildren(self, parentPageId):
        result = self.__confluence.get_page_by_id(page_id=parentPageId, expand="children")
        ##requestUrl = result['children']['_links']['self']
        requestUrl = "{}{}/search?start=0&limit=9999&cql=parent={}".format(
            self.__confluenceBaseUrl, self.__contentApiUrl, parentPageId)
        print(requestUrl)

        requestResponse = requests.get(
            requestUrl, auth=(self.__username, self.__password))
        print(requestResponse)
        return requestResponse.json()['results']

    def getPageBody(self, pageId):
        requestUrl = "{}/rest/api/content/{}?expand=body.storage".format(
            self.__confluenceBaseUrl, pageId)
        requestResponse = requests.get(
            requestUrl, auth=(self.__username, self.__password))
        return requestResponse.json()['body']['storage']['value']

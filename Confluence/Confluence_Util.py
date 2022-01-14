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


    


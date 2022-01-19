import requests
from atlassian import Confluence
import time


class Comala_Util:

    def __init__(self, baseUrl, userName, password):
        self.__contentApiUrl = '/rest/cw/1/content/'
        # Change these based on your instance
        self.__confluenceBaseUrl = baseUrl

        self.__username = userName
        self.__password = password

        

    def isDraft(self, pageId):

        requestUrl = "{}{}{}/status".format(self.__confluenceBaseUrl, self.__contentApiUrl,
            pageId)

        requestResponse = requests.get(requestUrl, auth=(self.__username, self.__password))
        if (requestResponse.status_code == 200):
            ##print(requestResponse.json())
            if requestResponse.json()['state']['name'] == "Draft":
                return True
        else:
            print("Request Failed with Status Code: {} on the page : {}".format(
                requestResponse.status_code, pageId))
        return False
    
    def isInitial(self, pageId):

        requestUrl = "{}{}{}/status".format(self.__confluenceBaseUrl, self.__contentApiUrl,
                                            pageId)

        requestResponse = requests.get(
            requestUrl, auth=(self.__username, self.__password))
        if (requestResponse.status_code == 200):
            ##print(requestResponse.json())
            print("Request Successful with Status Code: {} on the page : {}".format(
                requestResponse.status_code, pageId))
            if requestResponse.json()['state']['initial'] == True:
                return 1
            else:
                return 0 
        else:
            print("Request Failed with Status Code: {} on the page : {}".format(
                requestResponse.status_code, pageId))
        return -1

    def isFinal(self, pageId):

        requestUrl = "{}{}{}/status".format(self.__confluenceBaseUrl, self.__contentApiUrl,
                                            pageId)

        requestResponse = requests.get(
            requestUrl, auth=(self.__username, self.__password))
        if (requestResponse.status_code == 200):
            ##print(requestResponse.json())
            print("Request Successful with Status Code: {} on the page : {}".format(
                requestResponse.status_code, pageId))
            if requestResponse.json()['state']['final'] == True:
                return 1
            else:
                return 0
        else:
            print("Request Failed with Status Code: {} on the page : {}".format(
                requestResponse.status_code, pageId))
        return -1

    def getState(self, pageId):
        requestUrl = "{}{}{}/status".format(self.__confluenceBaseUrl, self.__contentApiUrl,
                                            pageId)

        requestResponse = requests.get(
            requestUrl, auth=(self.__username, self.__password))
        if (requestResponse.status_code == 200):
            ##print(requestResponse.json())
            print("Request Successful with Status Code: {} on the page : {}".format(
                requestResponse.status_code, pageId))
            return requestResponse.json()['state']['name']
            
        else:
            print("Request Failed with Status Code: {} on the page : {}".format(
                requestResponse.status_code, pageId))
        return "CW Not Found"

import requests
from atlassian import Confluence
import time
from getpass import getpass




class ConfiForm_Utils:
    def __init__(self, userName, password, confluenceBaseUrl, contentApi):
        self.__username = userName
        self.__password = password
        self.__contentApiUrl = contentApi
        self.__confluenceBaseUrl = confluenceBaseUrl
         

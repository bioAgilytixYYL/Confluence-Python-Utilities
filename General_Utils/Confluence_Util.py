from _typeshed import Self
import requests
from atlassian import Confluence
import time
from getpass import getpass

class Confluence_Utils(Self):


    self.__contentApiUrl = '/rest/api/content'
    # Change these based on your instance
    self.__confluenceBaseUrl = 'https://confluence.corp.bioagilytix.com/confluence'

def login():
    
    username = 'yangyang.liu'
    password = getpass("password")

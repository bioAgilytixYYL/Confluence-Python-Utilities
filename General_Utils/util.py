import requests
from atlassian import Confluence
import time
from getpass import getpass

contentApiUrl = '/rest/api/content'
# Change these based on your instance
confluenceBaseUrl = 'https://confluence.corp.bioagilytix.com/confluence'

def login():
    
    username = 'yangyang.liu'
    password = getpass("password")

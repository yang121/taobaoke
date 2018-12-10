'''
Created on 2012-6-29

@author: lihao
'''
from .api.base import sign
from .api import rest

class appinfo(object):
    def __init__(self, appkey, secret):
        self.appkey = appkey
        self.secret = secret

def getDefaultAppInfo():
    pass

     
def setDefaultAppInfo(appkey,secret):
    default = appinfo(appkey,secret)
    global getDefaultAppInfo 
    getDefaultAppInfo = lambda: default
    




    


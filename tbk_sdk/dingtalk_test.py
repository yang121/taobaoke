# -*- coding: utf-8 -*-
'''
Created on 2018-9-17

@author: xiaoxuan.lp
'''

from ..tbk_sdk.dingtalk import api

import api

request = api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
request.corpid="*******"
request.corpsecret="*******"

f = request.getResponse()
print(f)

request = api.OapiXiaoxuanPreTest1Request("https://oapi.dingtalk.com/topapi/xiaoxuan/pre/test1")
request.normalData="1"
request.systemData="2"

f = request.getResponse("******")
print(f)
    

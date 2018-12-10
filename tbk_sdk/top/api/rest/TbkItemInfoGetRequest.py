'''
Created by auto_sdk on 2018.11.10
'''
from ..base import RestApi
class TbkItemInfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ip = None
		self.num_iids = None
		self.platform = None

	def getapiname(self):
		return 'taobao.tbk_sdk.item.info.get'

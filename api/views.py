from django.shortcuts import render, HttpResponse, render_to_response
from tbk_sdk import top
from taobaoke.settings import *

# Create your views here.
def get_item(request):
    req = top.api.rest.TbkItemGetRequest(TBK_URL)
    req.set_app_info(top.appinfo(APPKEY, SECRET))

    req.fields = "num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
    req.q = "女装"
    req.cat = "16,18"
    req.itemloc = "杭州"
    req.sort = "tk_rate_des"
    req.is_tmall = 'false'
    req.is_overseas = 'false'
    req.start_price = 100
    req.end_price = 300
    req.start_tk_rate = 100
    req.end_tk_rate = 300
    req.platform = 1
    req.page_no = 1
    req.page_size = 1
    # try:
    resp = req.getResponse()
    print(resp)
    # except Exception as e:
    #     print(e.args)
    #     resp = 'error'

    return render(request, 'items.html', resp)
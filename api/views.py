from django.shortcuts import render, HttpResponse, render_to_response
from django.views import View
from tbk_sdk import top
from taobaoke.settings import *

class ItemView(View):
    fields = "num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity," \
                 "item_url,seller_id,volume,nick"

    def get(self, request):
        kwargs = request.GET.dict()

        resp = get_item_api(self.fields, **kwargs)

        return render(request, 'items.html', resp)

    def post(self, request):
        kwargs = request.POST.dict()

        if not kwargs.get('cat') and not kwargs.get('q'):
            kwargs['cat'] = '16, 18'

        resp = get_item_api(self.fields, **kwargs)

        return render(request, 'items.html', resp)


# 淘宝客商品查询
def get_item_api(fields, q=None, cat=None, itemloc=None, sort=None, is_tmall=False, is_overseas=False,
                 start_price=None, end_price=None, start_tk_rate=None, platform=1, page_no=1, page_size=10):
    """
    :api_name：taobao.tbk.item.get
    :param request: http://127.0.0.1:8000/api/item/%E5%A5%B3%E8%A3%85/16,18/%E6%9D%AD%E5%B7%9E/tk_rate/false/false/100/300/50/10/1/2
    :param q:查询词
    :param cat:后台类目ID，用,分割，最大10个，该ID可以通过taobao.itemcats.get接口获取到
    :param itemloc:所在地
    :param sort:排序_des（降序），排序_asc（升序），销量（total_sales），淘客佣金比率（tk_rate）， 累计推广量（tk_total_sales），总支出佣金（tk_total_commi）
    :param start_price:折扣价范围下限，单位：元
    :param end_price:折扣价范围上限，单位：元
    :param start_tk_rate:淘客佣金比率上限，如：1234表示12.34%
    :param end_tk_rate:淘客佣金比率下限，如：1234表示12.34%
    :param fields:需返回的字段列表，选填：num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick
    :param is_tmall:是否商城商品，设置为true表示该商品是属于淘宝商城商品，设置为false或不设置表示不判断这个属性
    :param is_overseas:是否海外商品，设置为true表示该商品是属于海外商品，设置为false或不设置表示不判断这个属性
    :param platform:链接形式：1：PC，2：无线，默认：１
    :param page_no:第几页，默认：１
    :param page_size:页大小，默认20，1~100
    :return:
        results	NTbkItem []		淘宝客商品
            num_iid	Number	123	商品ID
            title	String	连衣裙	商品标题
            pict_url	String	http://gi4.md.alicdn.com/bao/uploaded/i4/xxx.jpg	商品主图
            small_images	String[]	http://gi4.md.alicdn.com/bao/uploaded/i4/xxx.jpg	商品小图列表
            reserve_price	String	102.00	商品一口价格
            zk_final_price	String	88.00	商品折扣价格
            user_type	Number	1	卖家类型，0表示集市，1表示商城
            provcity	String	杭州	宝贝所在地
            item_url	String	http://detail.m.tmall.com/item.htm?id=xxx	商品地址
            nick	String	demo	卖家昵称
            seller_id	Number	123	卖家id
            volume	Number	1	30天销量
        total_results	Number	100	搜索到符合条件的结果总数
    """
    req = top.api.TbkItemGetRequest(TBK_URL)
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.fields = fields

    req.q = q
    req.cat = cat
    req.itemloc = itemloc
    req.sort = sort
    req.is_tmall = is_tmall
    req.is_overseas = is_overseas
    req.start_price = start_price
    req.end_price = end_price
    req.start_tk_rate = start_tk_rate
    req.platform = platform
    req.page_no = page_no
    req.page_size = page_size

    # try:
    resp = req.getResponse()
    # except Exception as e:
    #     print(e.args)
    #     resp = 'error'
    print(resp)
    return resp


# 淘宝客商品详情查询（简版）
def get_item_info_api(num_iids, platform=1, ip=None):
    """
    :param num_iids:商品ID串，用,分割，最大40个
    :param platform:链接形式：1：PC，2：无线，默认：１
    :param ip:ip地址，影响邮费获取，如果不传或者传入不准确，邮费无法精准提供
    :return:
        results	NTbkItem []		淘宝客商品
            cat_name	String	女装	一级类目名称
            num_iid	Number	123	商品ID
            title	String	连衣裙	商品标题
            pict_url	String	http://gi4.md.alicdn.com/bao/uploaded/i4/xxx.jpg	商品主图
            small_images	String[]	http://gi4.md.alicdn.com/bao/uploaded/i4/xxx.jpg	商品小图列表
            reserve_price	String	102.00	商品一口价格
            zk_final_price	String	88.00	商品折扣价格
            user_type	Number	1	卖家类型，0表示集市，1表示商城
            provcity	String	杭州	商品所在地
            item_url	String	http://detail.m.tmall.com/item.htm?id=xxx	商品链接
            seller_id	Number	123	卖家id
            volume	Number	1	30天销量
            nick	String	xx旗舰店	店铺名称
            cat_leaf_name	String	情趣内衣	叶子类目名称
            is_prepay	Boolean	true	是否加入消费者保障
            shop_dsr	Number	23	店铺dsr 评分
            ratesum	Number	13	卖家等级
            i_rfd_rate	Boolean	true	退款率是否低于行业均值
            h_good_rate	Boolean	true	好评率是否高于行业均值
            h_pay_rate30	Boolean	true	成交转化是否高于行业均值
            free_shipment	Boolean	true	是否包邮
            material_lib_type	String	1	商品库类型，支持多库类型输出，以“，”区分，1:营销商品主推库
    """
    req = top.api.TbkItemInfoGetRequest(TBK_URL)
    req.set_app_info(top.appinfo(APPKEY, SECRET))

    req.num_iids = num_iids
    req.platform = platform
    req.ip = ip

    # try:
    resp = req.getResponse()
    print(resp)
    return resp
    # except Exception, e:
    #     print(e)


# 获取淘抢购的数据，淘客商品转淘客链接，非淘客商品输出普通链接
def get_tqg_api(adzone_id, fields, start_time=None, end_time=None, page_no=1, page_size=20):
    """
    :api name: taobao.tbk.ju.tqg.get
    :param adzone_id: 推广位id
    :param fields: 需返回的字段列表: click_url,pic_url,reserve_price,zk_final_price,total_amount,sold_num,title,category_name,start_time,end_time
    :param start_time: 最早开团时间：2016-08-09 09:00:00
    :param end_time: 最晚开团时间：2016-08-09 16:00:00
    :param page_no: 第几页，默认1，1~100
    :param page_size: 页大小，默认40，1~40
    :return:
    """
    req = top.api.TbkJuTqgGetRequest(TBK_URL)
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.adzone_id = adzone_id
    # req.fields = "click_url,pic_url,reserve_price,zk_final_price,total_amount,sold_num,title,category_name,start_time,end_time"
    req.fields = fields
    # req.start_time = "2016-08-09 09:00:00"
    req.start_time = start_time
    # req.end_time = "2016-08-09 16:00:00"
    req.end_time = end_time
    req.page_no = page_no
    req.page_size = page_size
    # try:
    resp = req.getResponse()
    print(resp)
    # except Exception, e:
    #     print(e)
    return resp


# 好券清单API【导购】
def get_dg_item_coupon(adzone_id, q, cat='16,18', platform=1, page_no=1, page_size=20):
    """
    :api name: taobao.tbk.dg.item.coupon.get
    :param adzone_id: mm_xxx_xxx_xxx的第三位
    :param q: 查询词
    :param cat: 后台类目ID，用,分割，最大10个，该ID可以通过taobao.itemcats.get接口获取到
    :param platform: 1：PC，2：无线，默认：1
    :param page_no: 第几页，默认：1（当后台类目和查询词均不指定的时候，最多出10000个结果，即page_no*page_size不能超过10000；当指定类目或关键词的时候，则最多出100个结果）
    :param page_size: 页大小，默认20，1~100
    :return:
    results	TbkCoupon []		TbkCoupon
        small_images	String[]	http://img4.tbcdn.cn/tfscom/i3/TB1vPdxHXXXXXbtXpXXXXXXXXXX_!!2-item_pic.png	商品小图列表
        shop_title	String	秉迪数码专营店	店铺名称
        user_type	Number	1	卖家类型，0表示集市，1表示商城
        zk_final_price	String	158.00	折扣价
        title	String	zoyu kindle保护套 paperwhite1/2/3套958壳KPW3超薄皮套休眠499	商品标题
        nick	String	秉迪数码专营店	卖家昵称
        seller_id	Number	1779343388	卖家id
        volume	Number	4792	30天销量
        pict_url	String	http://img03.daily.taobao.net/tfscom/i1/TB1pBadNpXXXXbgaXXXXXXXXXXX_!!0-item_pic.jpg	商品主图
        item_url	String	http://item.taobao.com/item.htm?id=524136796550	商品详情页链接地址
        coupon_total_count	Number	8000	优惠券总量
        commission_rate	String	50.30	佣金比率(%)
        coupon_info	String	满16元减10元	优惠券面额
        category	Number	1	后台一级类目
        num_iid	Number	0	itemId
        coupon_remain_count	Number	6859	优惠券剩余量
        coupon_start_time	String	2016-09-25	优惠券开始时间
        coupon_end_time	String	2016-09-26	优惠券结束时间
        coupon_click_url	String	https://uland.taobao.com/coupon/edetail?e=XoElCPr3Ydt9%2BIHBh%2BrOiioPr%2BRaKTNCLYP29st3XV5ow2ATT0uODg13gui0W49o5PdvjO4eOnOie%2FpBy9wBFg%3D%3D&pid=mm_0_0_0&af=1&itemId=524136796550	商品优惠券推广链接
        item_description	String	夏季凉被 全棉亲肤	宝贝描述（推荐理由）
    total_results	Number	100	总请求数
    """
    req = top.api.TbkDgItemCouponGetRequest(TBK_URL)
    req.set_app_info(top.appinfo(APPKEY, SECRET))

    req.adzone_id = adzone_id
    req.q = q
    req.cat = cat
    req.platform = platform
    req.page_size = page_size
    req.page_no = page_no
    # try:
    resp = req.getResponse()
    print(resp)
    # except Exception, e:
    #     print(e)
    return resp


# 阿里妈妈推广券信息查询。传入商品ID+券ID，或者传入me参数，均可查询券信息。
def get_coupon(me=None, item_id=None, activity_id=None):
    req = top.api.TbkCouponGetRequest(TBK_URL)
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.me = me
    req.item_id = item_id
    req.activity_id = activity_id

    # try:
    resp = req.getResponse()
    print(resp)
    # except Exception, e:
    #     print(e)

    return resp


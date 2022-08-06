import requests
import json
import time
import os

CookieJDs = os.environ["JD_COOKIE"].split('&')
print(CookieJDs)
num=1

def jfdh(key, pin):
    jfurl = "https://lop-proxy.jd.com/JingIntegralApi/transfer"
    jfheaders = {
        "Host": "lop-proxy.jd.com",
        "content-length": "147",
        "lop-dn": "jingcai.jd.com",
        "app-key": "jexpress",
        "access": "H5",
        "client": "android",
        "eid": "",
        "osversion": "10",
        "networktype": "wifi",
        "x-requested-with": "XMLHttpRequest",
        "event-id": "c8bc11c0-cfb5-4379-a4e4-362c461485be",
        "d_model": "V1914A",
        "partner": "vivo",
        "clientversion": "11.1.2",
        "appparams": "{\"appid\":158,\"ticket_type\":\"m\"}",
        "biz-type": "service-monitor",
        "source-client": "2",
        "uuid": "165890770769094320084",
        "area": "5_264_277_49656",
        "sdkversion": "1.0.7",
        "user-agent": "jdapp;android;11.1.2;;;appBuild/98157;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1659457129466%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22CWC1ZtLrZwU3DWG5EJvrEG%3D%3D%22%2C%22od%22%3A%22DNZvEWYzYzG1DNG3YJC1CtG1ZtYyEJHrEWSyY2UzEWVvC2HwCNLtYzVtDtC5ENTsCwO2YtPrYJqmCJLvCwDtZG%3D%3D%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22CWC1ZtLrZwU3DWG5EJvrEG%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; V1914A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046011 Mobile Safari/537.36",
        "screen": "360*780",
        "jexpress-trace-id": "a2d7713d-f5e1-4c4e-bf15-f588dc69468d",
        "build": "98157",
        "clientinfo": "{\"appName\":\"jingcai\",\"client\":\"m\"}",
        "accept": "application/json, text/plain, */*",
        "jexpress-report-time": "1659457146095",
        "forcebot": "0",
        "d_brand": "vivo",
        "content-type": "application/json;charset\u003dutf-8",
        "version": "1.0.0",
        "origin": "https://jingcai-h5.jd.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://jingcai-h5.jd.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
        "cookie": "pt_key={}".format(key)
    }
    jfdata = [{"pin": "{}".format(pin), "businessNo": "7a199a16-0beb-4f99-bdb0-8758cafc9fad", "type": "1",
               "transferNumber": "100", "title": "京豆兑换物流积分"}]
    dhjf = requests.post(url=jfurl, headers=jfheaders, data=json.dumps(jfdata)).text
    print(dhjf)


def jddh(key, pin):
    jdurl = "https://lop-proxy.jd.com/JingIntegralApi/transfer"
    jdheaders = {
        "Host": "lop-proxy.jd.com",
        "content-length": "147",
        "lop-dn": "jingcai.jd.com",
        "app-key": "jexpress",
        "access": "H5",
        "client": "android",
        "eid": "",
        "osversion": "10",
        "networktype": "wifi",
        "x-requested-with": "XMLHttpRequest",
        "event-id": "dff6de06-3dda-4ed8-8446-544d4f5f5614",
        "d_model": "V1914A",
        "partner": "vivo",
        "clientversion": "11.1.2",
        "appparams": "{\"appid\":158,\"ticket_type\":\"m\"}",
        "biz-type": "service-monitor",
        "source-client": "2",
        "uuid": "165890770769094320084",
        "area": "5_264_277_49656",
        "sdkversion": "1.0.7",
        "user-agent": "jdapp;android;11.1.2;;;appBuild/98157;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1658938008592%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22CWC1ZtLrZwU3DWG5EJvrEG%3D%3D%22%2C%22od%22%3A%22DNZvEWYzYzG1DNG3YJC1CtG1ZtYyEJHrEWSyY2UzEWVvC2HwCNLtYzVtDtC5ENTsCwO2YtPrYJqmCJLvCwDtZG%3D%3D%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22CWC1ZtLrZwU3DWG5EJvrEG%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; V1914A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046011 Mobile Safari/537.36",
        "screen": "360*780",
        "jexpress-trace-id": "17375c62-0e51-40d9-870a-ed761e2e2729",
        "build": "98157",
        "clientinfo": "{\"appName\":\"jingcai\",\"client\":\"m\"}",
        "accept": "application/json, text/plain, */*",
        "jexpress-report-time": "1658938026541",
        "forcebot": "0",
        "d_brand": "vivo",
        "content-type": "application/json;charset\u003dutf-8",
        "version": "1.0.0",
        "origin": "https://jingcai-h5.jd.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://jingcai-h5.jd.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
        "cookie": "pt_key={}".format(key)
    }
    jddata = [{"pin": "{}".format(pin), "businessNo": "538862a4-fbd6-48e4-8a8e-8d2c9bb6673d", "type": "2",
               "transferNumber": "100", "title": "物流积分兑换京豆"}]
    dhjd = requests.post(url=jdurl, headers=jdheaders, data=json.dumps(jddata)).text
    print(dhjd)


if __name__ == "__main__":
    for i in CookieJDs:
        key=i.split("pt_key=")[1].split(";")[0]
        pin=i.split("pt_pin=")[1].split(";")[0]
        print("开始第{}个账号".format(num),"账号名为{}".format(pin))
        jfdh(key,pin)
        time.sleep(5)
        jddh(key,pin)
        time.sleep(5)
        num=num+1
    print("执行结束")

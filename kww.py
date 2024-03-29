import json
import time
import hashlib
import random
import requests

db = '{"1":1,"2":1,"3":1,"4":1,"5":4,"6":1,"7":1,"8":1,"9":1,"10":1,"11":1,"12":1,"13":2,"14":1,"15":2,"16":1,"17":2,"18":2,"19":1,"20":1,"21":4,"22":1,"23":4,"24":1,"25":3,"26":1,"27":4,"28":1,"29":4,"30":4,"31":1,"32":4,"33":1,"34":1,"35":1,"36":1,"37":4,"38":1,"39":3,"40":4,"41":2,"42":1,"43":2,"44":4,"45":4,"46":2,"47":1,"48":1,"49":1,"50":2,"51":4,"52":4,"53":1,"54":3,"55":3,"56":4,"57":4,"58":4,"59":1,"60":4,"61":1,"62":1,"63":1,"64":2,"65":1,"66":3,"67":1,"68":1,"69":4,"70":4,"71":4,"72":1,"73":4,"74":2,"75":4,"76":4,"77":4,"78":1,"79":2,"80":1,"81":2,"82":3,"83":3,"84":4,"85":1,"86":2,"87":3,"88":2,"89":4,"90":2,"91":4,"92":3,"93":4,"94":2,"95":3,"96":2,"97":3,"98":2,"99":4,"100":4,"101":4,"102":3,"103":4,"104":4,"105":4,"106":4}'
qb = eval(db)

print("开始")
#
# 少跑几个号醒来看结果
import os
uidlist = os.environ["kwwCookies"].split("\n")
timesalt = int(round(time.time() * 1000))


# 获取用户id
def hqid(ck):
    url = "https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/answer/start.do?user_type=1&is_from_share=1&_t={}".format(
        timesalt)
    headers = {
        "Host": "89420.activity-20.m.duiba.com.cn",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/index.html?appID=89420&from=login&spm=89420.1.1.1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-us,en",
        "Cookie": "{}".format(ck)
    }
    res = requests.post(url=url, headers=headers).text
    html = json.loads(res)
    print(html)
    return html['data']


# 获取链接
def lianjie(uid):
    url = 'https://member.kwwblcj.com/member/api/info/?userKeys=v1.0&pageName=loginFreePlugin&formName=searchForm&uid={}&levelCode=2&redirect=https%3A%2F%2F89420.activity-20.m.duiba.com.cn%2Fprojectx%2Fp129446ea%2Findex.html%3FappID%3D89420&actionType=%E6%AF%8F%E6%97%A5%E7%AD%94%E9%A2%98&actionDesc=https%3A%2F%2F89420.activity-20.m.duiba.com.cn%2Fprojectx%2Fp129446ea%2Findex.html%3FappID%3D89420&objId=C05&memberId={}'.format(
        uid, uid)
    headers = {
        "Host": "member.kwwblcj.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "content-type": "application/json",
        "user-paramname": "memberId",
        "user-random": "{}".format(nonce),
        "user-sign": "{}".format(signature),
        "user-timestamp": "{}".format(timestamp),
        "Referer": "https://servicewechat.com/wxfb0905b0787971ad/42/page-frame.html",
        "Accept-Encoding": "gzip, deflate"
    }
    res = requests.get(url=url, headers=headers).text
    html = json.loads(res)
    return html['result']


# 获取ck

def cookie(lianjie):
    url = '{}'.format(lianjie)
    print(url)
    headers = {
        "Host": "89420.activity-20.m.duiba.com.cn",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-us,en"
    }
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    cookie = str(res.cookies)
    wdata4 = cookie.split("<Cookie wdata4=")[1].split(" for")[0]
    time = cookie.split("<Cookie w_ts=")[1].split(" for")[0]
    ck = "wdata4={}; w_ts={};".format(wdata4, time)
    print(ck)
    return ck


# 获取题目
def hqtm(ck, yhid):
    try:
        # "https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/answer/getQuestion.do?startId=19091166&user_type=0&is_from_share=1&_t=1665659697772"
        url = 'https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/answer/getQuestion.do?startId={}&user_type=0&is_from_share=1&_t={}'.format(
            yhid, timesalt)
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "{}".format(ck),
            "Host": "89420.activity-20.m.duiba.com.cn",
            "Referer": "https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/index.html?appID=89420&from=login&spm=89420.1.1.1",
            "sec-ch-ua": "\"Chromium\";v=\"106\", \"Microsoft Edge\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36 Edg/106.0.1370.37"
        }
        res = requests.get(url=url, headers=headers).text
        print(res)
        html = json.loads(res)
        print(html['data']['id'])
        return html['data']['id']
    except Exception as e:
        print(e)


# GET /projectx/p129446ea/answer/submit.do?answer=4&startId=136755714&timestamp=1671150076626&sign=b41600555d264423dcf4f44aaca4f4f2&user_type=1&is_from_share=1&_t=1671150076627 HTTP/1.1
# 回答题目
def hdtm(key, ck, yhid):
    try:
        url = 'https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/answer/submit.do?answer={}&startId={}&timestamp={}&sign={}&user_type=1&is_from_share=1&_t={}'.format(
            key, yhid, timesalt, answerSign, timesalt + 1)
        print(url)
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "{}".format(ck),
            "Host": "89420.activity-20.m.duiba.com.cn",
            "Referer": "https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/index.html?appID=89420&from=login&spm=89420.1.1.1",
            "sec-ch-ua": "\"Chromium\";v=\"106\", \"Microsoft Edge\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36 Edg/106.0.1370.37"
        }
        res = requests.get(url=url, headers=headers).text
        print(res)
        html = json.loads(res)
        return html['data']['id'], html['data']['correctAnswer']
    except Exception as e:
        print(e)


def chaxun(id):
    try:
        idd = "{}".format(id)
        print(qb[idd])
        return qb[idd]
    except:
        print("没有查询到这道题的正确答案")
        return 10


# def gengxin(correct):
#     try:
#         sql = 'INSERT INTO kwwtk VALUES({},{})'.format(correct[0], correct[1])
#         count = mycursor.execute(sql)
#         mydb.commit()
#     except Exception as e:
#         print(e)


# 提交答案
def tj(ck, yhid):
    url = "https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/answer/complete.do?startId={}&user_type=1&is_from_share=1&_t={}".format(
        yhid, timesalt)
    headers = {
        "Host": "89420.activity-20.m.duiba.com.cn",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/index.html?appID=89420&from=login&spm=89420.1.1.1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-us,en",
        "Cookie": "{}".format(ck)
    }
    res = requests.get(url=url, headers=headers)
    print(res.text)


def getSign(uid):
    l = ["A", "Z", "B", "Y", "C", "X", "D", "T", "E", "S", "F", "R", "G", "Q", "H", "P", "I", "O", "J", "N", "k", "M",
         "L",
         "a", "c", "d", "f", "h", "k", "p", "y", "n"]
    timestamp = getTimestamp()
    nonce = random.randint(0, 31)
    data = "{}{}{}".format(timestamp, uid, l[nonce])
    signature = hashlib.md5(data.encode()).hexdigest()
    return timestamp, nonce, signature


def getTimestamp():
    timestamp = int(time.time() * 1000)
    return timestamp


def getSalt():
    url = "https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/coop_frontVariable.query?user_type=1&is_from_share=1&_t={}".format(
        getTimestamp())
    headers = {
        "Host": "89420.activity-20.m.duiba.com.cn",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://89420.activity-20.m.duiba.com.cn/projectx/p129446ea/index.html?appID=89420&from=login&spm=89420.1.1.1",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-us,en",
        "Cookie": "{}".format(ck)
    }
    html = requests.get(url=url, headers=headers).json()
    salt = html['data']['salt']
    return salt


def getAnswerSign():
    timestamp = getTimestamp()
    c = "{}{}{}{}".format(salt, yhid, key, timestamp)
    print(c)
    sign = hashlib.md5(c.encode()).hexdigest()
    print(sign)
    return timestamp, sign


if __name__ == '__main__':
    for uid in uidlist:
        timestamp, nonce, signature = getSign(uid)
        lj = lianjie(uid)
        ck = cookie(lj)
        yhid = hqid(ck)
        for i in range(5):
            id = hqtm(ck, yhid)
            print(id)
            key = chaxun(id)
            salt = getSalt()
            timesalt, answerSign = getAnswerSign()
            correct = hdtm(key, ck, yhid)
            # gengxin(correct)
        tj(ck, yhid)
        print("结束")

# 百度贴吧签到
# 设置变量bdtbcookie为百度贴吧cookie ck用@分割多个ck 青龙格式expor bdtbcookie="odahsudh971hdw1h9gdv1bihd8917b9d1hf1bwf1b@waefudihsaofiybdioasjnfbiodayfsdafdsaudfidaso"
# 设置变量bdtbqdmc为想要签到的贴吧名用@分割 青龙格式export bdtbqdmc="显卡&图拉丁"
import requests
import os
import time
import json

bdtbck = os.getenv('bdtbcookie')
bdtbqd = os.getenv('bdtbqdmc')
bdtbqds = list(str("%s" % bdtbqd).split("@"))
bdtbcks = list(str("%s" % bdtbck).split("@"))
print("===================百度贴吧签到脚本=====================")
time_tuple = time.localtime(time.time())
print("北京时间:{}年{}月{}日{}点{}分{}秒".format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4],
                                       time_tuple[5]))
print("======================================================")
for n in range(len(bdtbcks)):
    print("正在执行第%d个账号" % n)
    for i in range(len(bdtbqds)):
        url = 'https://tieba.baidu.com/sign/add'
        bdtbqd = bdtbqds[i]
        print("正在执行签到的贴吧：%s" % bdtbqd)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39',
            'cookie': ("%s" % bdtbcks), }
        data = {
            'ie': 'utf - 8',
            "kw": ("%s" % bdtbqd)
        }
        html = requests.post(url=url, headers=headers, data=data).text
        req = json.loads(html)
        no = (req['no'])
        if no == 0:
            req = req['data']
            print(req['errmsg'])
        else:
            print(req['error'])

        print("======================================================")
        if i == (len(bdtbqds) - 1):
            print("")
        else:
            print("两秒后继续签到下一个")
        time.sleep(2)

start_time = time.time()
sum = 0
for i in range(1000000):
    sum += i
end_time = time.time()
print("脚本运行结束 运行时间：%f" % (end_time - start_time))
# print(html)

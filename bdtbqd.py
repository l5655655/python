import requests
import os


bdtbck = os.getenv('bdtbcookie')
bdtbqd = os.getenv('bdtbqdmc')
bdtbqds=list(str("%s" % bdtbqd).split("&"))
print(bdtbqds)
for i in range(len(bdtbqds)):
    url = 'https://tieba.baidu.com/sign/add'
    bdtbqd=bdtbqds[i]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39',
        'cookie': ("%s" % bdtbck), }
    data = {
        'ie': 'utf - 8',
        "kw": ("%s" % bdtbqd)
    }
    html = requests.post(url=url, headers=headers, data=data).text
    print(html.encode().decode("unicode_escape"))

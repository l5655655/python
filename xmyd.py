# 设置环境变量xmyd="账号@密码"
# 格式为export xmyd="11111111111@111111111"
# 使用脚本前请先注册小米运动运动账号并授权微信或支付宝,才可以刷成功
# 修改步数范围在脚本里面,预设为10000到20000步
import requests
import json
import random
import os
xmydck = list(str(os.getenv('xmyd')).split("@"))
xmydzh=xmydck[0]
xmydmm=xmydck[1]
step=random.randint(10000,20000)
url = 'http://mi.5655655.top/MiStepApi?user={}&password={}&step={}'.format(xmydzh,xmydmm,step)
html = requests.get(url=url).text
req = json.loads(html)
print("成功修改步数"+str(step)+"步")

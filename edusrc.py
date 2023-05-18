#edusrc积分变动提醒
#by ekkoo
import requests
import re
import json
def rankchange():
    global url, response, headers, rank, name
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    url = "https://src.sjtu.edu.cn/profile/15013/"
    response1 = requests.get(url, headers=headers).text
    rank1 = re.findall(r'Rank： .*', response1)
    name1 = re.findall(r'<h3 class="am-panel-title am-fl">.*', response1)
    name2=str(name1) #split函数只支持字符串类型截取
    name=name2.split('>',1)[1].split('的')[0]#截取用户名
    while(1):
        response = requests.get(url,headers=headers).text
        rank = re.findall(r'Rank： .*', response)
        print(rank)
        if(rank!=rank1):
            text_title = name+'您的EDUSRC漏洞审核通过啦(*^▽^*)'
            text_content = "在另一条时间线里，这么做是对的  \n 加油！少年\n"+"\n 详情请点击"+url
            sendKey = 'SCT210463TFGHBI8F8NZgpOQDxZSSpXW01'

            url = f"https://sctapi.ftqq.com/{sendKey}.send"
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            data = {
                'text': f"{text_title}",
                'content': f"{text_content}"
            }
            response = requests.post(url, data=data)
            if json.loads(response.text)["data"]['error'] == 'SUCCESS':
                 print("消息推送成功")
            break
        else:
            print("服务正在运行中...")

rankchange()

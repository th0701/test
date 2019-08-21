'''
封装请求方法
'''

import json
import requests
from common import log_conf
from common import readconf


logs = log_conf.MyLog()

def ji(fuc):

    def fc(*args):
        try:
            data = fuc(*args)
            return data
        except Exception as a:
            logs.error(a)
            raise Exception("接口请求失败")
    return fc

@ji
def doget(url ,param = None):
    di = requests.get(url,params=param, timeout=0.01).json()
    if di.get("resultcode")== "200":
        return "请求成功!"
    else:
        return "请求数据失败!"

@ji
def dopost(url ,param = None):
    di = requests.post(url,data=param, timeout=2).json()
    if di.get("resultcode")== "200":
        return "请求成功!"
    else:
        return "请求数据失败!"
@ji
def doRequest(param1):
    weath = requests.get(readconf.url, params=param1)
    if weath.status_code == 200:
        weath_content = weath.json()
        resultcode = weath_content.get("resultcode")
        reason = weath_content.get("reason")
        return resultcode,reason







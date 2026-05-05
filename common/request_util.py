import requests
from config.config import BASE_URL


# 这个文件负责统一发送请求。
# headers=None 的意思是：默认不传请求头；如果接口需要 token、Content-Type，再传 headers。
# params=None 的意思是：默认没有参数。

def send_get(path, params=None, headers=None):
    url = BASE_URL + path
    res = requests.get(url=url, params=params, headers=headers)
    # 把请求结果返回给测试用例继续使用。
    return res


def send_post(path, json=None, headers=None):
    url = BASE_URL + path
    res = requests.post(url=url, json=json, headers=headers)
    return res
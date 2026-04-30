import requests



# 这个文件负责统一发送请求。
# headers=None 的意思是：默认不传请求头；如果接口需要 token、Content-Type，再传 headers。
# params=None 的意思是：默认没有参数。

def send_get(url, params=None, headers=None):
    res = requests.get(url, params=params, headers=headers)
    # 把请求结果返回给测试用例继续使用。
    return res


def send_post(url, json=None, headers=None):
    res = requests.post(url, json=json, headers=headers)
    return res
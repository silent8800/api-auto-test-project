import requests
from config.config import BASE_URL
from common.log_util import get_logger


logger = get_logger()

# 这个文件负责统一发送请求。
# headers=None 的意思是：默认不传请求头；如果接口需要 token、Content-Type，再传 headers。
# params=None 的意思是：默认没有参数。

def send_get(path, params=None, headers=None):
    url = BASE_URL + path

    logger.info(f"发送GET请求，url={url}, params={params}, headers={headers}")

    try:
        res = requests.get(url=url, params=params, headers=headers)
    # 把请求结果返回给测试用例继续使用。
        logger.info(f"响应状态码：{res.status_code}")
        logger.info(f"响应内容：{res.text[:500]}")
        return res
    except Exception as e:
        logger.error(f"GET请求异常：{e}")
        raise


def send_post(path, json=None, headers=None):
    url = BASE_URL + path
    logger.info(f"发送POST请求，url={url}, json={json}, headers={headers}")

    try:
        res = requests.post(url=url, json=json, headers=headers)
        logger.info(f"响应状态码：{res.status_code}")
        logger.info(f"响应内容：{res.text}")
        return res

    # 表示如果请求过程出错，就把错误记录到日志里。
    except Exception as e:
        logger.error(f"POST请求异常：{e}")

        # 表示记录完日志后，错误继续抛给
        # pytest，让测试结果正常显示失败，不会被日志代码偷偷吞掉。
        raise
#执行后日志记录
# 请求地址
# 请求参数
# 请求头
# 响应状态码
# 响应内容
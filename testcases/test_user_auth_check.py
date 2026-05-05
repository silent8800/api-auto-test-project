from common.request_util import send_get

# 用户鉴权相关接口测试用例
def test_get_user_with_auth(auth_headers):


    res = send_get("/get", headers=auth_headers)
    print("状态码：", res.status_code)
    print("响应头：", res.headers.get("Content-Type"))
    print("响应内容：", res.text)

    data = res.json()

    assert res.status_code == 200
    assert data["headers"]["Authorization"] == "Bearer order_token_001"
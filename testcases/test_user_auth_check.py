import allure
from common.request_util import send_get

# 用户鉴权相关接口测试用例

@allure.feature("用户管理模块")
@allure.story("Token 鉴权")
@allure.title("用户接口 Token 鉴权测试")
def test_get_user_with_auth(auth_headers):
    res = send_get("/get", headers=auth_headers)

    data = res.json()

    assert res.status_code == 200
    assert data["headers"]["Authorization"] == "Bearer order_token_001"

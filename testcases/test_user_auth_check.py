from common.request_util import send_get

# 测token / header是否携带成功
def test_get_user_with_auth(auth_headers):
    url = "https://httpbin.org/get"

    res = send_get(url, headers=auth_headers)

    data = res.json()

    assert res.status_code == 200
    assert data["headers"]["Authorization"] == "Bearer order_token_001"
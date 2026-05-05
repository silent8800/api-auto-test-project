import pytest
from common.request_util import send_post

# 管理公共前置条件。
@pytest.fixture(scope="module")
def auth_headers():


    login_body = {
        "username": "api_test_01",
        "password": "123456",
        "token": "order_token_001"
    }

    login_res = send_post("/post", json=login_body)
    login_data = login_res.json()

    token = login_data["json"]["token"]

    headers = {
        "Authorization": "Bearer " + token
    }

    return headers
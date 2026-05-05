from common.request_util import send_get
from common.db_util import query_one

# 校验token / header是否携带成功

def test_user_auth_mysql_check(auth_headers):
    # 1. 准备接口地址和参数
    url = "/get"

    params = {
        "username": "alice",
        "id": "1"
    }

    # 2. 使用封装的 send_get，带上 conftest.py 里的 auth_headers
    res = send_get("/get", params=params, headers=auth_headers)

    api_data = res.json()

    # 3. 从接口响应里提取字段
    api_username = api_data["args"]["username"]
    api_id = int(api_data["args"]["id"])


    # 登录获取
    # token，然后生成公共请求头。
    # 4. 校验请求头是否带成功
    assert res.status_code == 200
    assert api_data["headers"]["Authorization"] == "Bearer order_token_001"

    # 5. 使用接口返回字段查询 MySQL
    sql = "select id, username, city, role, status from user where id = %s and username = %s"

    result = query_one(sql, (api_id, api_username))

    print(result)

    # 6. 校验数据库数据
    assert result is not None
    assert api_id == result["id"]
    assert api_username == result["username"]
    assert result["city"] == "Taipei"
    assert result["role"] == "tester"
    assert result["status"] == 1


# conftest 准备 headers → send_get 发请求 → res.json 提取字段 → query_one 查库 → assert 校验一致性
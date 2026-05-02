from common.request_util import send_get
from common.db_util import query_one


def test_user_info_by_mysql():
    # 1. 准备接口请求参数
    params = {
        "username": "alice",
        "id": 1
    }

    # 2. 发送 GET 请求
    res = send_get("https://httpbin.org/get", params=params)

    # 3. 断言状态码
    assert res.status_code == 200

    # 4. 提取接口返回数据
    data = res.json()
    api_username = data["args"]["username"]
    api_id = int(data["args"]["id"])

    # 5. 查询数据库
    sql = "select id, username, city, role, status from user where username = %s and id = %s"
    result = query_one(sql, (api_username, api_id))

    # 6. 断言数据库查询结果不为空
    assert result is not None

    # 7. 校验接口数据和数据库数据一致
    assert result["username"] == api_username
    assert result["id"] == api_id
    assert result["city"] == "Taipei"
    assert result["role"] == "tester"
    assert result["status"] == 1
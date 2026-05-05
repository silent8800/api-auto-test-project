from common.request_util import send_get
from common.db_util import query_one

#接口返回数据与 MySQL 数据库数据一致性校验

def test_api_mysql_user_by_util():
    url = "/get"
# 2. params 传 username=alice, id=1
    params = {
        "username": "alice",
        "id": "1"
    }
# 1. 使用 send_get() 请求 https://httpbin.org/get
    #请求封装
    res = send_get("/get", params=params)

    api_data = res.json()
# 3. 从接口响应里提取 username 和 id
    api_username = api_data["args"]["username"]
    api_id = int(api_data["args"]["id"])

    # 4. 使用 query_one() 查询 user 表
    sql = "select id, username, city, role, status from user where username = %s and id = %s"

    result = query_one(sql, (api_username, api_id))

    print(result)
    # 5. 校验接口 id == 数据库 id
    # 6. 校验接口 username == 数据库 username
    # 7. 校验数据库 city == Taipei
    # 8. 校验数据库 role == tester
    # 9. 校验数据库 status == 1


    assert result is not None
    assert res.status_code == 200
    assert api_id == result["id"]
    assert api_username == result["username"]
    assert result["city"] == "Taipei"
    assert result["role"] == "tester"
    assert result["status"] == 1

    # request_util.py
    # 负责封装接口请求方法，比如
    # send_get()、send_post()，底层还是调用
    # requests.get()、requests.post()。测试用例只需要传
    # url、params、headers，就能发送请求。

    # db_util.py
    # 负责封装数据库操作，比如连接
    # MySQL、创建
    # cursor、执行
    # SQL、返回查询结果。query_one()
    # 是里面的一个公共查询方法。

    # test_api_mysql_user_by_util.py,测试用例文件负责组织测试流程：准备接口参数，调用
    # send_get()
    # 发请求，提取接口返回字段，调用
    # query_one()
    # 查数据库，最后用
    # assert 做接口数据和数据库数据的一致性校验。
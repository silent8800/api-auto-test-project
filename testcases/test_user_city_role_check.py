from common.request_util import send_get
from common.db_util import query_one


# 按 city + role 多条件查询并进行数据库校验


def test_user_city_role_check():
    url = "/get"

    params = {
        "city": "Taipei",
        "role": "tester"
    }
    # 使用封装的 GET 请求方法发接口请求
    res = send_get("/get", params=params)

    api_data = res.json()
    # 3. 从接口响应里提取 city和role
    api_city = api_data["args"]["city"]
    api_role = api_data["args"]["role"]

    # 根据接口返回的 city 和 role 查询数据库
    sql =  "select id,username,city,role,status from user where city = %s and role = %s limit 1"

    result = query_one(sql, (api_city, api_role))
    print(result)

    #断言校验即可
    assert result is not None
    assert res.status_code == 200
    assert api_city == result["city"]
    assert api_role == result["role"]
    assert result["status"] == 1

     #result[]。字典的key来自SQL查询出来的列名
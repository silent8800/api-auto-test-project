import pytest
import allure
from common.request_util import send_get
from common.db_util import query_one


@allure.feature("用户管理模块")
@allure.story("用户信息查询")
@allure.title("用户信息查询接口数据驱动测试")
@pytest.mark.parametrize(
    "username, user_id, city, role",
    [
        ("data_user_01", 21, "Taipei", "tester"),
        ("data_user_02", 22, "Taichung", "developer"),
        ("data_user_03", 23, "Kaohsiung", "admin"),
    ]
)
def test_user_info_data_driven(username, user_id, city, role):
    params = {
        "username": username,
        "id": user_id,
        "city": city,
        "role": role
    }

    res = send_get("/get", params=params)

    assert res.status_code == 200

    data = res.json()
    api_username = data["args"]["username"]
    api_id = int(data["args"]["id"])
    api_city = data["args"]["city"]
    api_role = data["args"]["role"]

    sql = """
        select id, username, city, role, status
        from user
        where username = %s and id = %s
    """

    result = query_one(sql, (api_username, api_id))

    assert result is not None
    assert result["username"] == api_username
    assert result["id"] == api_id
    assert result["city"] == api_city
    assert result["role"] == api_role
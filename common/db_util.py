import pymysql
from config.config import DB_CONFIG
# 把 MySQL 连接代码封装成函数
def query_one(sql, params=None):
    #连接mysql数据库
    # 把字典里的数据库配置拆开传进去。
    conn = pymysql.connect(**DB_CONFIG)
    # 让db_util.py查询结果返回字典
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

    cursor.execute(sql, params)
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result
    # 4. 使用 DictCursor，让查询结果以字典形式返回   查询后后面变字典形式
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(sql, params)

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

def get_user_by_id(user_id):
    sql = "select id, username, city, role, status from user where id = %s"
    return query_one(sql, (user_id,))
def get_user_by_user_id(order_id):
    sql = "select id,user_id,amount,order_date from order where user_id = %s"
    return query_one(sql, (order_id,))
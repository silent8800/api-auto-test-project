import pymysql

# 把 MySQL 连接代码封装成函数
def query_one(sql, params=None):
    #连接mysql数据库
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="silent",
        charset="utf8mb4"
    )
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
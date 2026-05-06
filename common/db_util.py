import pymysql
from config.config import DB_CONFIG
from common.log_util import get_logger


logger = get_logger()

# 把 MySQL 连接代码封装成函数


def query_one(sql, params=None):


    logger.info(f"执行SQL：{sql}, 参数：{params}")
    #连接mysql数据库
    # 把字典里的数据库配置拆开传进去。

    conn = pymysql.connect(**DB_CONFIG)
    # 让db_util.py查询结果返回字典

    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

    cursor.execute(sql, params)
    result = cursor.fetchone()
    logger.info(f"SQL查询结果：{result}")
    # 以后数据库查不到数据，你就可以通过日志看到：

    # 执行了哪条SQL传了什么参数查询结果是什么

    cursor.close()
    conn.close()
    return result


def get_user_by_id(user_id):
    sql = "select id, username, city, role, status from user where id = %s"
    return query_one(sql, (user_id,))
def get_user_by_user_id(order_id):
    sql = "select id,user_id,amount,order_date from order where user_id = %s"
    return query_one(sql, (order_id,))
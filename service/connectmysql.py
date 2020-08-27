"""
连接数据库
"""
import pymysql
from config import ip, sql_user, sql_password


class DB:
    def __init__(self, host=ip, port=3306, db='nky', user=sql_user, passwd=sql_password, charset='utf8'):
        # 建立连接 
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型        
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标        
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行        
        self.conn.commit()
        # 关闭游标        
        self.cur.close()
        # 关闭数据库连接        
        self.conn.close()


if __name__ == '__main__':
    with DB() as db:
        sql = "SELECT name,adjustment,actual,frozen,transit,available FROM budget_item WHERE `name` = '" + "养老保险" + "';"
        db.execute(sql)
        bd = list(db)[0]
    print("预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s" %
                  (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
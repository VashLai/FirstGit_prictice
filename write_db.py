"""
    write_db.py
    pymysql寫操作示例(insert update delete)
"""

import pymysql

# 連接資料庫
db = pymysql.Connect(host='localhost',
                     port=3306,
                     user='root',
                     password='a123456',
                     database='stu',
                     charset='utf8')

# 獲取游標   (操作資料庫，執行SQL語句）
cur = db.cursor()


# 寫入資料庫
try:
    """
    # sql語句執行
    # 插入操作
    name = input('Name:')
    age = input('Age:')
    score = input('Score:')
    sql = "insert into class (name,age,score) \
          values(%s, %s, %s)"
    cur.execute(sql, [name, age, score])
    """

    """
    # 修改操作
    sql = "update interest set price = 11800 where name = 'Tt'"
    """

    # 刪除操作
    sql = "delete from class where Join_time is null"

    cur.execute(sql)
    db.commit()

except Exception as e:
    db.rollback()  # 退回到commit之前的資料庫狀態
    print(e)

# 關閉資料庫
cur.close()
db.close()

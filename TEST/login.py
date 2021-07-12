"""
编写一个程序模拟注册和登录的过程

   * 创建一个user表 包含 用户名和密码字段
     create table user (id int primary key auto_increment,name varchar(32) not null,passwd varchar(32) not null);


   * 应用程序中模拟注册和登录功能

     注册则输入用户名密码将用户名密码存入到数据库
     （用户名不能重复）

     登录则进行数据库比对，如果有该用户则打印登录成功
     否则让重新输入

"""
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='a123456',
                     database='login',
                     charset='utf8')
cur = db.cursor()
sql = ['select account,password from user where account = %s',
       'insert into user value(%s,%s)']


def check(account):
    cur.execute(sql[0], [account])
    data = cur.fetchone()
    if data:
        return data
    # else:
    #     return


def register():
    while True:
        account = input("請輸入註冊帳號：")
        if check(account):
            print("帳號存在，請重新輸入！！")
            continue
        password = input("請輸入註冊密碼：")
        try:
            cur.execute(sql[1], [account, password])
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
            continue
        print("註冊完成")
        return


def login():
    while True:
        account = input("登入帳號：")
        data = check(account)
        if not data:
            print("帳號不存在，請重新輸入")
            continue
        while True:
            password = input("登入密碼：")
            if password == data[1]:
                print("登入成功")
                return
            else:
                print("密碼錯誤，請重新輸入")
                continue


def menu():
    while True:
        print("""
              =========================
              a、註冊   b、登入    q、結束
              =========================
        """)
        choice = input("請輸入代號：")
        if choice == 'a':
            register()
        elif choice == 'b':
            login()
        elif choice == 'q':
            cur.close()
            db.close()
            return
        else:
            print("輸入錯誤，請重新輸入")
            continue


if __name__ == "__main__":
    menu()

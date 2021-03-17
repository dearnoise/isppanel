import pymysql
from modules.dbapi import dbapi

creds = {"host": "",
         "port": ,
         "user": "",
         "password": "",
         "db_name": ""}

mysql_con = MySqlConnector(creds)


# Тестируем добавление строки.
insert_string = '''insert into users(full_name, address, balance, login, password, ppoe_ip, extra)
                   values(%s,%s,%s,%s,%s,%s,%s);'''
mysql_con.update(insert_string, ("Булат Ольга Ильинична", "Тверь, пр. Коммунизма, д. 6, кв. 353", 0, 423724, "123456", "10.13.6.1", "Опытный пользователь ПК"))

# Тестируем выборку одного пользователя.
model_string = '''select * from users where id= %s;'''
model_data = mysql_con.queryall(model_string, 0)
print(model_data)
